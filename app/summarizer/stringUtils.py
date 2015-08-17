# -*- coding: utf8 -*-

import re
from nltk import tokenize, corpus, data, pos_tag

# set env
data.path.append("nltk_data")

def to_unicode(object):
    """Return a unicode object"""    
    if isinstance(object, unicode):
        return object
    elif isinstance(object, bytes):
        return object.decode("utf8")
    elif hasattr(object, "__unicode__"):
        return bytes(object).decode("utf8")
    elif hasattr(object, "__unicode__"):
        return unicode(instance)
    else: 
        raise TypeError("this object cannot be converted to unicode")

def sent_tokenize(text):
    """Return tokenized sentences"""    
    text = to_unicode(text)

    # spaces
    text = re.sub(r"\s\s+", " ", text)

    # single quotes
    text = text.replace(u"\u2018", "'")
    text = text.replace(u"\u2019", "'")

    # double quotes
    text = text.replace(u"\u201c", "")
    text = text.replace(u"\u201d", "")

    return tuple(token.strip() for token in tokenize.sent_tokenize(text))

def word_tokenize(text):
    """Return tokenized words"""    
    tokens = tokenize.word_tokenize(text.lower())
    return tuple(tokens)