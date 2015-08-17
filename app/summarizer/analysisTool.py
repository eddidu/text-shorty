import math
import collections

from app.summarizer.document import Document, Sentence

def compute_tf(sentence):
    """Return tf of the given *sentence*."""
    return collections.Counter(sentence.words)

def compute_idf(sentences):
    """Return idf of the given *sentences*."""
    n = len(sentences)

    idf = {}
    for s1 in sentences:
        for word in s1.words:
            if word not in idf:
                n_d = sum(1 for s2 in sentences if word in s2.words)
                idf[word] = math.log(n / n_d)

    return idf
