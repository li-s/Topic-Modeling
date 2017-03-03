import gensim
import pickle

def make_comparison():
	id2word = gensim.corpora.Dictionary.load('./datasets/lda.model.id2word')

	lda = gensim.models.ldamodel.LdaModel(num_topics=20, id2word=id2word)
	lda.load('./datasets/lda.model')

	print(lda)
	with open('./data/short_text_vectors.txt', 'rb') as a:
		read = pickle.load(a)
		doc_lda =[]
		for i in range(0, len(read)):
			doc_lda.append(lda[read[i]])
		print(doc_lda)

make_comparison()
