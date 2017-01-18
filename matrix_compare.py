import pickle
from time import time

def matrix_compare(matrix):
	numerator = 0
	denominator = 0
	for i in range(0, len(matrix[0])):
		numerator += matrix[0][i]*matrix[1][i]
	
	a = 0
	b = 0
	for i in range(0, len(matrix[0])):
		a += matrix[0][i]**2
		b += matrix[1][i]**2
	denominator = a**0.5 * b**0.5

	return numerator/denominator
	
if __name__ == '__main__':
	start1 = time()
	with open('./data/matrix(byte).txt', 'rb') as aa:
		a = pickle.load(aa)
		print('They are: ' + str(matrix_compare(a)) + ' apart')
	print('Time taken: {}'.format(time() - start1))
