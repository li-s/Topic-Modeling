from gensim import corpora
from collections import defaultdict
from pprint import pprint
import re
from time import time
import pickle
import enchant
from nltk.stem.snowball import SnowballStemmer
	
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
	dictionary.save_as_text('datasets/the_short_dictionary.txt')
	dictionary.save('datasets/the_short_dictionary.dict')
	corpus = [dictionary.doc2bow(text) for text in texts] 
	corpora.MmCorpus.serialize('datasets/the_short_corpus.mm', corpus)
	return corpus
	
if __name__ == '__main__':
	start1 = time()
	with open('./data/short_texts.txt', 'r') as read:
		text = read.readlines()
	with open('./data/short_text_vectors.txt', 'wb') as w:
		pickle.dump(make_dict(text), w)
	print('Program ran for: {}'.format(time()-start1))
