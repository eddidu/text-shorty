import collections
import operator
import math

from app.summarizer.document import Document, Sentence
from app.summarizer import analysisTool
from app.summarizer import stringUtils


class KeywordsExtractor(object):
    """Extracts keywords from a document"""

    def compute_tf(self, sentences):
        """Return the tf for entire sentences"""
        tf = collections.Counter()
        for sentence in sentences:
            tf += analysisTool.compute_tf(sentence)

        return tf    

    def compute_ratings(self, sentences):
        """Return the ratings of words"""
        tf = self.compute_tf(sentences)
        idf = analysisTool.compute_idf(sentences)

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
        ratings = self.compute_ratings(document.sentences)
        result = self.pick_keywords(ratings, 5)

        return tuple(result)