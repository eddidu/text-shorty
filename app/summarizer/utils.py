from nltk import tokenize, corpus, data

# set env
data.path.append('nltk_data')

def instance_to_unicode(instance):
    if hasattr(instance, '__unicode__'):
        return unicode(instance)
    elif hasattr(instance, '__str__'):
        return bytes(instance).decode('UTF-8')

    return to_unicode(repr(instance))

def to_unicode(object):
    if isinstance(object, unicode):
        return object
    elif isinstance(object, bytes):
        return object.decode("utf8")
    
    return instance_to_unicode(object)
'''
	TODO: tokenizer failed to split sentences when a sentence ends with special characters(usually quotes.)
	TODO: deal with \n inside sentences
'''
def to_sentences(text):
	processed_text = to_unicode(text)
	return [s.strip() for s in tokenize.sent_tokenize(processed_text)]

'''
	TODO: take langugaes other than english
'''
def to_words(text):
	stop_words = set(corpus.stopwords.words('english'))
	words = tokenize.word_tokenize(text)
	filtered_words = [word.lower() for word in words if (word.lower() not in stop_words) and (word.isalpha())] 
	return filtered_words