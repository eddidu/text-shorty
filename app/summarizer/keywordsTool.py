import collections
import operator
import math

from app.summarizer import analysisTool
from app.summarizer import stringUtils


class KeywordsExtractor(object):
    """Extracts keywords from a document"""

    def compute_tf(self, token_vectors):
        """Return the tf for entire sentences"""
        tf = collections.Counter()
        for v in token_vectors:
            tf += analysisTool.compute_tf(v)

        return tf    

    def compute_ratings(self, token_vectors):
        """Return the ratings of words"""
        tf = self.compute_tf(token_vectors)
        idf = analysisTool.compute_idf(token_vectors)

        rating = {}
        for word in tf:
            rating[word] = tf[word] * idf[word]

        return rating

    def pick_keywords(self, ratings, numKeywords):
        """Return pick keywords using ratings"""
        numCandidates = len(ratings)

        if numKeywords == 0:
            raise ValueError("requested number of keywords shouldn't be zero")

        if numKeywords >= numCandidates:
            raise ValueError(
                "requested number of keywords {} shouldn't be >= candidates {}".format(numKeywords, numCandidates)
            )
        
        sorted_ratings = sorted(ratings.items(), key=operator.itemgetter(1), reverse=True)

        return [w[0] for w in sorted_ratings[0:numKeywords]]

    def extract(self, document):
        """Return keywords"""
        # tokenize text
        sentences = stringUtils.sent_tokenize(document)
        tokens = [stringUtils.word_tokenize(s) for s in sentences]

        #TODO: need to pos tag words for picking only nouns
        #TODO: need to stem tokens for improving accuracy
        ratings = self.compute_ratings(tokens)
        result = self.pick_keywords(ratings, 5)

        return tuple(result)