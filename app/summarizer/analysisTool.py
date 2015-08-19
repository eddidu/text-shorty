import math
import collections

def compute_tf(tokens):
    """Return tf of the given *tokens*."""
    return collections.Counter(tokens)

def compute_idf(token_vectors):
    """Return idf of the given *token vectors*."""
    n = len(token_vectors)

    idf = {}
    for v1 in token_vectors:
        for word in v1:
            if word not in idf:
                n_d = sum(1 for v2 in token_vectors if word in v2)
                idf[word] = math.log(n / n_d)

    return idf
