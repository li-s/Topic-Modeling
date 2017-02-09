from pprint import pprint
import pickle
from time import time
#4134 unique tokens

def adder(a_text):
	b = ''.join(a_text)
	remove = ['']
	texts = [text for text in b.split('\n') if text not in remove]
	
	document = []
	for i in range(0, len(texts)):
		a = texts[i].split()
		document.append(a)
	texts = document	#makes a list with the lines in the previous txt as sub lists

	document = []
	i = 0
	while i < len(texts):
		try:
			number = 0
			number = int(texts[i][2])
			position = i
			while int(texts[position][0]) == int(texts[position+1][0]):
				number += int(texts[position+1][2])
				position += 1
			i = position
				
		except:
			pass
		
		document.append('{}\t{}\t{}'.format(str(texts[position][0]), str(texts[position][1]), str(number)))
		
		i += 1

	print(i)
	texts = document
	document = []
	for line in texts:
		document.append(line.split('\t'))
	texts = document
	return texts
	
if __name__ == '__main__':
	start1 = time()
	with open('./data/intermediate_lda.txt', 'wb') as w:
		with open('./data/intermediate_doc.txt', 'r') as read:
			pickle.dump(adder(read), w)
	
	with open('./data/use_this_lda.txt', 'w') as w:
		with open('./data/intermediate_lda.txt', 'rb') as a:
			read = pickle.load(a)
			for i in range(0, len(read)):
				w.write(str(read[i][0]) + '	' + str(read[i][1]) + '	' + str(read[i][2]) + '\n')
	print('The program took: {}'.format(time()-start1))
	
	

