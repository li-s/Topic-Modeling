import gensim
import pickle

id2word = gensim.corpora.Dictionary.load('./datasets/lda.model.id2word')

lda = gensim.models.ldamodel.LdaModel(num_topics=20, id2word=id2word)
lda.load('./datasets/lda.model')

print(lda)
with open('short_texts.txt', 'rb') as a:
	read = pickle.load(a)
	doc_lda = lda[read]
