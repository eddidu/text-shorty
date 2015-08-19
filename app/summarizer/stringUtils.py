# -*- coding: utf8 -*-

import re
import nltk

# set env
nltk.data.path.append("nltk_data")

def to_unicode(object):
    """Return a unicode object"""
    result = None
    if isinstance(object, unicode):
        result = object
    elif isinstance(object, bytes):
        result = object.decode("utf8")
    elif hasattr(object, "__unicode__"):
        result = bytes(object).decode("utf8")
    elif hasattr(object, "__unicode__"):
        result = unicode(instance)
    else: 
        raise TypeError("this object cannot be converted to unicode")

    return result

def sent_tokenize(text):
    """Return tokenized sentences"""    
    text = to_unicode(text)

    # spaces
    text = re.sub(r"\s\s+", " ", text)

    # single quotes
    text = text.replace(u"\u2018", "'")
    text = text.replace(u"\u2019", "'")

    # double quotes
    text = text.replace(u"\u201c", "\"")
    text = text.replace(u"\u201d", "\"")

    return tuple(token.strip() for token in nltk.tokenize.sent_tokenize(text))

def word_tokenize(text, language="english", filter_stopwords=True, stem=False):
    """Return tokenized words"""    
    tokens = nltk.tokenize.word_tokenize(text.lower())

    # remove non-alphanumeric tokens
    # TODO: instead of using isalnum(), string.punctuations + expand contractions may be used here
    tokens = [t for t in tokens if t.isalnum()]

    if filter_stopwords:
        stopwords = set(nltk.corpus.stopwords.words(language))
        tokens = [t for t in tokens if t not in stopwords]

    if stem:
        stemmer = nltk.stem.lancaster.LancasterStemmer()
        tokens = [stemmer.stem(t) for t in tokens]

    return tuple(tokens)