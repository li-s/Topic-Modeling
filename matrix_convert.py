from pprint import pprint
from time import time
import pickle

def matrix_convert(text, dictionary):

	w = len(dictionary)
	h = 2
	matrix = [[0 for x in range(w)] for y in range(h)]
	
	for i in range(0, len(text[0])):
		matrix[0][text[0][i][0]] = text[0][i][1]
	for i in range(0, len(text[1])):
		matrix[1][text[1][i][0]] = text[1][i][1]
		
	return matrix


if __name__ == '__main__':
	start1 = time()
	with open('matrix.txt', 'wb') as aa:
		with open('my_edit.txt', 'r') as bb:
			with open('number.txt', 'rb') as pickle_file:
				a = pickle.load(pickle_file)
				b = bb.readlines()
				pickle.dump(matrix_convert(a, b), aa)
	
	with open('matrix2.txt', 'w') as aa:
		with open('my_edit.txt', 'r') as bb:
			with open('number.txt', 'rb') as pickle_file:
				a = pickle.load(pickle_file)
				b = bb.readlines()
				pprint(matrix_convert(a,b), stream = aa)
	print('Time taken: {}'.format(time() - start1))
