from gensim import corpora
from collections import defaultdict
from pprint import pprint
import re
from time import time
import pickle
import enchant
from nltk.stem.snowball import SnowballStemmer

def identify():
	all_positions = []
	with open('./data/text_vectors(byte).txt', 'rb') as read:
		texts = pickle.load(read)
		
		for i in range(len(texts)):
			if len(texts[i]) < 10:
				all_positions.append(i)
	print(all_positions)
	return all_positions
	
	
def select(position, a_text):
	document = []
	for i in position:
		document.append(a_text[i])
		
	texts = document
	texts = [[token for token in text]for text in texts]

	dictionary = corpora.Dictionary(texts)
	dictionary.save_as_text('datasets/the_short_dictionary.txt')
	dictionary.save('datasets/the_short_dictionary.dict')
	corpus = [dictionary.doc2bow(text) for text in texts] 
	corpora.MmCorpus.serialize('datasets/the_short_corpus.mm', corpus)

	return None
if __name__ == '__main__':
	start1 = time()
	with open('./data/raw_pruned_texts(byte).txt', 'rb') as b:
		read = pickle.load(b)
		a = identify()
		select(a, read)
	print('Program ran for: {}'.format(time()-start1))
