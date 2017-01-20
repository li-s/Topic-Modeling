import gensim
import bz2


id2word = gensim.corpora.Dictionary.load_from_text#('./data/extracted_texts.txt')



	# load corpus iterator
mm = gensim.corpora.MmCorpus('./datasets/the_corpus.mm') #Is fine

#print(mm)

print('1')

#lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=0, passes=20)
