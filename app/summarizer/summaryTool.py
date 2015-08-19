import numpy
import math
import operator
import collections

from app.summarizer import analysisTool
from app.summarizer import stringUtils

class LexrankSummarizer(object):
    """Summarization tool using lexrank algorithm."""    

    def __init__(self):
        self._treshold = 0.1
        self._epsilon = 0.001

    def compute_cosine(self, token_vectors, treshold):
        """Return squre matrix of size len(token_vectors) 
            with each element represents cosine similarities of corresponding sentences
        """
        n = len(token_vectors)

        tf = [analysisTool.compute_tf(v) for v in token_vectors]
        idf = analysisTool.compute_idf(token_vectors)

        cosine_matrix = numpy.zeros((n, n))

        for row in xrange(n):
            for col in xrange(row, n):

                v1 = token_vectors[row]
                v2 = token_vectors[col]

                # diagonal values set to 1
                if row == col:
                    cosine_matrix[row][col] = 1
                    continue

                # sentences with only few words are skipped since 
                # they tend to get higher scores
                if len(v1) < 3 or len(v2) < 3:
                    continue 

                common_words = set(v1) & set(v2)
                # no common words means numerator = 0
                if len(common_words) == 0:
                    continue

                numerator = sum(tf[row][word] * tf[col][word] * pow(idf[word], 2) for word in common_words)

                d1 = sum(pow(tf[row][word] * idf[word], 2) for word in v1)
                d2 = sum(pow(tf[col][word] * idf[word], 2) for word in v2)
                denominator = math.sqrt(d1) * math.sqrt(d2)
                
                if numerator > 0  and numerator / denominator > treshold:
                    cosine_matrix[row][col] = 1.0
                    cosine_matrix[col][row] = 1.0

        return cosine_matrix

    def normalize_matrix(self, matrix):    
        """Return normalized matrix"""
        for i, row in enumerate(matrix):
            row_total = sum(row)
            
            if row_total != 0:
                matrix[i] = [j / row_total for j in row]

        return matrix

    def compute_ratings(self, matrix, epsilon):
        """Return ratings as a vector"""    
        size = len(matrix)

        transposed_matrix = numpy.transpose(matrix)
        current_p = [1.0 / size] * size
        prev_p = [0.0] * size

        while True:
            prev_p = current_p
            current_p = numpy.dot(transposed_matrix, current_p)
            error = sum(pow(current_p[x] - prev_p[x], 2) for x in xrange(size))
            
            if error < pow(epsilon, 2):
                break

        return current_p  

    def pick_best_sentences(self, sentences, ratings, numSentences):
        """Return sentences that best represents the document"""
        n = len(sentences)

        if numSentences == 0:
            raise ValueError("requested number of sentences shouldn't be zero")

        if numSentences >= n:
            raise ValueError(
                "requested number of sentences {} shouldn't be >= candidates {}".format(numSentences, n)
            )

        # sort by rank
        ranked_sentences = sorted(zip(xrange(n), ratings, sentences), key=operator.itemgetter(1), reverse=True)    
        # sort by the order of the original sentences
        best_sentences = sorted(ranked_sentences[0:numSentences], key=operator.itemgetter(0))

        return [s[2] for s in best_sentences]

    def summarize(self, document, summaryLength):
        """Return a list of sentences"""
        # tokenize text
        sentences = stringUtils.sent_tokenize(document)
        tokens = [stringUtils.word_tokenize(s, stem=True) for s in sentences]

        cosine_matrix = self.compute_cosine(tokens, self._treshold)
        normalized_cosine_matrix = self.normalize_matrix(cosine_matrix)
        ratings = self.compute_ratings(normalized_cosine_matrix, self._epsilon)

        result = self.pick_best_sentences(sentences, ratings, summaryLength)

        return tuple(result)