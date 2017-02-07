import gensim
import bz2
from pprint import pprint

#id2word1 = gensim.corpora.Dictionary.load_from_text('./data/use_this_lda.txt')
id2word2 = gensim.corpora.Dictionary.load('./datasets/the_dictionary.dict')


	# load corpus iterator
mm = gensim.corpora.MmCorpus('./datasets/the_corpus.mm') #Is fine

print(mm)


#lda1 = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word1, num_topics=3, update_every=0, passes=20)

lda2 = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word2, num_topics=20, update_every=0, passes=20)


#lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)

print(lda1)
#pprint(lda1.print_topics(3))
pprint(lda2.print_topics(20))
