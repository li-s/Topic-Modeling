import gensim
import bz2
from pprint import pprint

def lda(a, b):
	location1 = './datasets/' + str(a)
	id2word = gensim.corpora.Dictionary.load(location1)


	# load corpus iterator
	location2 = './datasets/' + str(b)
	mm = gensim.corpora.MmCorpus(location2) #Is fine


	lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=20, update_every=0, passes=20)

	lda.save('./datasets/lda.model')

	pprint(lda.print_topics(20))
	
if __name__ == '__main__':
	b = input('Corpus(.mm): ')
	a = input('Dictionary(.dict): ')
	lda(a, b)
