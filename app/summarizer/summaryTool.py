import numpy
import math
import operator
import collections

from app.summarizer.document import Document, Sentence
from app.summarizer import analysisTool

class LexrankSummarizer(object):
    """Summarization tool using lexrank algorithm."""    

    def __init__(self):
        self._treshold = 0.1
        self._epsilon = 0.001

    def compute_cosine(self, sentences, treshold):
        """Return n * n matrix that represents cosines of the sentences 
            TODO: create tf * idf matrix for each term in every sentence where tf-idf[nth sentence][wordk] = tf * idf value
            TODO: find a way to deal with a short sentence which likely to get more votes..
        """       
        n = len(sentences)

        tf = [analysisTool.compute_tf(sentence) for sentence in sentences]
        idf = analysisTool.compute_idf(sentences)

        cosine_matrix = numpy.zeros((n, n))

        for row in xrange(n):
            for col in xrange(row, n):

                w1 = sentences[row].words
                w2 = sentences[col].words

                # diagonal values set to 1
                if row == col:
                    cosine_matrix[row][col] = 1
                    continue

                common_words = set(w1) & set(w2)
                # no common words means numerator = 0
                if len(common_words) == 0:
                    continue

                numerator = sum(tf[row][word] * tf[col][word] * pow(idf[word], 2) for word in common_words)

                d1 = sum(pow(tf[row][word] * idf[word], 2) for word in w1)
                d2 = sum(pow(tf[col][word] * idf[word], 2) for word in w2)
                denominator = math.sqrt(d1) * math.sqrt(d2)
                
                if numerator > 0  and numerator / denominator > treshold:
                    cosine_matrix[row][col] = 1.0
                    cosine_matrix[col][row] = 1.0

        return self.normalize_matrix(cosine_matrix)

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

    def pick_best_sentences(self, sentences, ratings, length):
        """Return sentences that best represents the document"""
        n = len(sentences)
        # sort by rank
        ranked_sentences = sorted(zip(xrange(n), ratings, sentences), key=operator.itemgetter(1), reverse=True)    
        # sort by the order of the original sentences
        best_sentences = sorted(ranked_sentences[0:length], key=operator.itemgetter(0))

        return [s[2].text for s in best_sentences]

    def summarize(self, document, summaryLength):
        """Return a list of sentences"""
        cosine_matrix = self.compute_cosine(document.sentences, self._treshold)
        ratings = self.compute_ratings(cosine_matrix, self._epsilon)

        result = self.pick_best_sentences(document.sentences, ratings, summaryLength)

        return tuple(result)