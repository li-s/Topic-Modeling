from gensim import corpora
from collections import defaultdict
from pprint import pprint
import re
from time import time
import pickle
import enchant
from nltk.stem.snowball import SnowballStemmer

def identify(text):
	all_positions = []
	for i in range(len(text)):
		if len(text[i]) <= 8:
			all_positions.append(i)
	return all_positions
	
def select(a_text, position):
	texts = ' '.join(a_text)
	remove = ('a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, ii, iii, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0'.split(', '))  
	remove_white_space = ['']
	
	texts = [word.lower() for word in re.split('\W', texts) if(word.lower() not in remove) 			and (word not in remove_white_space)]
	
	texts = ' '.join(texts)
	texts = texts.split('abcdefghijklmnopqrstuvwxyzzz')
	
	stemmer = SnowballStemmer("english")	
	texts = [stemmer.stem(text) for text in texts]
	
	document = []
	for i in position:
		document.append(texts[i])

	return document
	
def make_dict(a_text):
	texts = a_text
	
	en_word_pattern = re.compile('[a-z]+')
	texts = [[token for token in text if en_word_pattern.match(token)]for text in texts]
	english = enchant.Dict()
	texts = [[token for token in text if english.check(token)]for text in texts]
	
	stemmer = SnowballStemmer("english")	
	texts = [[stemmer.stem(token) for token in text] for text in texts]

	frequency = defaultdict(int)
	for text in texts:
		for token in text:
			frequency[token] += 1
	texts = [[token for token in text if frequency[token]>1]for text in texts]
	
	
	dictionary = corpora.Dictionary(texts)
	dictionary.save_as_text('datasets/the_shirt_dictionary.txt')
	dictionary.save('datasets/the_short_dictionary.dict')
	corpus = [dictionary.doc2bow(text) for text in texts] 
	corpora.MmCorpus.serialize('datasets/the_short_corpus.mm', corpus)


	return corpus
	
if __name__ == '__main__':
	start1 = time()
	with open('./data/raw_pruned_texts(byte).txt', 'rb') as b:
		read = pickle.load(b)
		positions = identify(read)
	with open('short_texts.txt', 'w') as w:
		with open('./data/extracted_texts.txt', 'r') as b:
			text = select(b, positions)
			pprint(text, stream = w)
	print('Step1: {}'.format(time()-start1))
	with open('./data/short_text_vectors.txt', 'wb') as w:
		pickle.dump(make_dict(text), w)
	print('Program ran for: {}'.format(time()-start1))
