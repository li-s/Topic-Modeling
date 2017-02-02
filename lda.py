import gensim
import bz2
from time import time

id2word = gensim.corpora.Dictionary.load_from_text('./data/use_this_lda.txt')



	# load corpus iterator
mm = gensim.corpora.MmCorpus('./datasets/the_corpus.mm') #Is fine

print(mm)


#lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=0, passes=20)

lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)

print(lda)
lda.print_topics(20)
