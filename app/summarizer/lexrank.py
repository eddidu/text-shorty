import numpy

import math, operator, collections

from app.summarizer import utils

class LexrankSummarizer(object):

	def __init__(self):
		self._treshold = 0.1
		self._epsilon = 0.001

	'''
	tf[nth sentence][term i] = frequency i 
	'''
	def compute_tf(self, word_tokenized_sentences):
		tf = []
		for s in word_tokenized_sentences:
			tf.append(collections.Counter(s))	

		return tf

	'''
	idf[term] = idf value of the term
	'''
	def compute_idf(self, word_tokenized_sentences):
		n = len(word_tokenized_sentences)
		idf = {}
		for s1 in word_tokenized_sentences:
			for term in s1:
				if term not in idf:
					n_d = sum(1 for s2 in word_tokenized_sentences if term in s2)
					idf[term] = math.log(n / n_d)	

		return idf

	'''
	TODO: create tf * idf matrix for each term in every sentence where tf-idf[nth sentence][wordk] = tf * idf value
	TODO: find a way to deal with a short sentence which likely to get more votes..
	'''
	def compute_cosine(self, word_tokenized_sentences, treshold):
		n = len(word_tokenized_sentences)	

		tf = self.compute_tf(word_tokenized_sentences)
		idf = self.compute_idf(word_tokenized_sentences)

		cosine_matrix = numpy.zeros((n, n))

		# this matrix is orthogonal with its values set 1 if row = column
		for row in xrange(n):
			for col in xrange(row, n):

				# diagonal values set to 1
				if row == col:
					cosine_matrix[row][col] = 1
					continue

				# sentences with only 1 meaningful term will be likely to get more votes...
				# so the cosine value is set to 0
				if len(word_tokenized_sentences[row]) < 2 or len(word_tokenized_sentences[col]) < 2:
					continue

				common_terms = set(word_tokenized_sentences[row]) & set(word_tokenized_sentences[col])
				# no common terms mean numerator = 0
				if len(common_terms) == 0:
					continue

				numerator = sum(tf[row][term] * tf[col][term] * pow(idf[term], 2) for term in common_terms)

				d1 = sum(pow(tf[row][term] * idf[term], 2) for term in word_tokenized_sentences[row])
				d2 = sum(pow(tf[col][term] * idf[term], 2) for term in word_tokenized_sentences[col])
				denominator = math.sqrt(d1) * math.sqrt(d2)
				
				if numerator > 0  and numerator / denominator > treshold:
					cosine_matrix[row][col] = 1.0
					cosine_matrix[col][row] = 1.0

		return self.normalize_matrix(cosine_matrix)

	def normalize_matrix(self, matrix):	
		# all row contain at least one 1(which is the result of self comparison)
		# if not... then something is wrong here
		for i, row in enumerate(matrix):
			row_total = sum(row)
			matrix[i] = [j / row_total for j in row]
		return matrix

	def compute_ratings(self, matrix, epsilon):
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
		n = len(sentences)
		# sort by rank
		ranked_sentences = sorted(zip(xrange(n), ratings, sentences), key=operator.itemgetter(1), reverse=True)	
		# sort by the order of the original sentences
		best_sentences = sorted(ranked_sentences[0:length], key=operator.itemgetter(0))

		return [s[2] for s in best_sentences]

	def summarize(self, article, summaryLength):
		sentences = utils.to_sentences(article)
		word_tokenized_sentences = []
		for s in sentences:
			word_tokenized_sentences.append(utils.to_words(s))

		cosine_matrix = self.compute_cosine(word_tokenized_sentences, self._treshold)
		ratings = self.compute_ratings(cosine_matrix, self._epsilon)

		result = self.pick_best_sentences(sentences, ratings, summaryLength)

		return result
