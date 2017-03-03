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

	texts = ' '.join(a_text)
	remove = ('the, be, to, of, and, a, in, that, have, i, it, for, not, on, with, he, as, you, do, at, n, www, html, http, ref, org, was, is, s, are, were, by, titl, or, ii, iii, d, x, b, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0'.split(', '))

	texts = [word.lower() for word in re.split('\W', texts) if(word.lower() not in remove)]

	en_word_pattern = re.compile('[a-z]+')
	texts = [word for word in texts if en_word_pattern.match(word)]
	english = enchant.Dict()
	texts = [token for token in texts if english.check(token)]

	stemmer = SnowballStemmer("english")
	texts = [stemmer.stem(token) for token in texts]

	doc = []
	doc.append(texts)
	doc2 = []
	doc.append(doc2)
	texts = doc
	print(texts)

	dictionary = corpora.Dictionary(texts)
	dictionary.save_as_text('../datasets/the_short_dictionary.txt')
	dictionary.save('../datasets/the_short_dictionary.dict')
	corpus = [dictionary.doc2bow(text) for text in texts]
	corpora.MmCorpus.serialize('../datasets/the_short_corpus.mm', corpus)
	return corpus

if __name__ == '__main__':
	start1 = time()
	with open('../data/short_texts.txt', 'r') as read:
		text = read.readlines()
	with open('../data/short_text_vectors.txt', 'wb') as w:
		pickle.dump(make_dict(text), w)
	print('Program ran for: {}'.format(time()-start1))
