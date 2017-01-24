import gensim
import bz2


id2word = gensim.corpora.Dictionary.load_from_text('./data/test.txt')



	# load corpus iterator
mm = gensim.corpora.MmCorpus('./datasets/the_corpus.mm') #Is fine

print(mm)


lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=0, passes=20)

print(lda)
