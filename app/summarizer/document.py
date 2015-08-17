from app.summarizer import stringUtils

class Document(object):
    """A document represent the text that will be analyzed as a whole 
    
    Attributes:
        sentences: tokenized sentences of this document

    """

    def __init__(self, text):
        sentences = []

        tokens = stringUtils.sent_tokenize(text)
        for t in tokens:
            sentence = Sentence(t)   
            sentences.append(sentence)

        self.sentences = tuple(sentences)

class Sentence(object):
    """A sentence is a wrapper class containig the text of a tokenized sentence
        and tokenized terms

    Attributes:
        text: text of this sentence
        words: tokenized words of this sentence

    """

    def __init__(self, text):
        self.text = text
        self.words = stringUtils.word_tokenize(text)

