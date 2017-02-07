import pickle
from time import time

start1 = time()
with open('./data/g_format_doc.txt', 'w') as w:
	with open('./data/pruned_texts(byte).txt', 'rb') as a:
		with open('./data/text_vectors.txt', 'rb') as b:
			
			dictionary = pickle.load(a)
			texts = pickle.load(b)
			
			dictionary_inverse = {y:x for x,y in dictionary.items()}
			dictionary = dictionary_inverse
			
			for i in range(len(texts)):
				for n in range(len(texts[i])):
					if texts[i][n][0] in dictionary:

						w.write(str(texts[i][n][0]) + ' ' + dictionary[texts[i][n][0]] + ' '+ str(texts[i][n][1])+'\n')
print('The program took: {}'.format(time()-start1))
