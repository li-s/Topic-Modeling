from gensim import corpora
from collections import defaultdict
from pprint import pprint
import re
from time import time
import pickle
import enchant
from nltk.stem.snowball import SnowballStemmer


def remove(a_text, number):
	texts = ' '.join(a_text)
	remove = ('the, be, to, of, and, a, in, that, have, i, it, for, not, on, with, he, as, you, do, at, n, www, html, http, ref, org, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0'.split(', '))    #20 most common english words + web urls
	remove_white_space = ['']
	
	texts = [word.lower() for word in re.split('\W', texts) if(word.lower() not in remove) 			and (word not in remove_white_space)]
	
	texts = ' '.join(texts)
	texts = texts.split('abcdefghijklmnopqrstuvwxyzzz')
	
	document = []
	for i in range(0, len(texts)-1):
		a = texts[i].split()
		document.append(a)
	texts = document
	
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
	dictionary.save('datasets/the_dictionary.dict')
	corpus = [dictionary.doc2bow(text) for text in texts] 
	corpora.MmCorpus.serialize('datasets/the_corpus.mm', corpus)

	if number == 1:
		return dictionary.token2id
	elif number == 2:
		return corpus
	else:
		return 1

if __name__ == '__main__':
	
	start1 = time()
	with open('./data/pruned_texts.txt', 'w') as a:
		with open('./data/extracted_texts.txt', 'r') as b:
			pprint(remove(b, 1), stream = a)

	with open('./data/text_vectors.txt', 'wb') as a:
		with open('./data/extracted_texts.txt', 'r') as b:
			pickle.dump(remove(b, 2), a)
	print('The program took: {}'.format(time() - start1))
