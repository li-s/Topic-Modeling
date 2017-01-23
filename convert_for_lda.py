import pickle

with open('./data/g_format_doc.txt', 'w') as w:
	with open('./data/pruned_texts(byte).txt', 'rb') as a:
		with open('./data/text_vectors.txt', 'rb') as b:
			
			dictionary = pickle.load(a)
			texts = pickle.load(b)
			
			for pairs in dictionary:
				for i in range(len(texts)):
					for n in range(len(texts[i])):
						if texts[i][n][0] == dictionary[pairs]:	
							w.write(str(dictionary[pairs]) + '\t' + pairs + '\t'+ str(texts[i][n][1])+'\n')
