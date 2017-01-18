import pickle
from time import time
from pprint import pprint
from prune import remove

def cos(text):	
	x = 0
	y = 0
	numerator = 0
	denominator = 0
	
	while x <= len(text[0])-1 and y <= len(text[1])-1:
		if	text[0][x][0] > text[1][y][0]:
			y += 1
		elif text[0][x][0] < text[1][y][0]:
			x +=1
		elif text[0][x][0] == text[1][y][0]:
			numerator += text[0][x][1]*text[1][y][1]
			x += 1
			y += 1

	a = 0
	b = 0
	for i in range(0, len(text[0])):
		a += (text[0][i][1])**2
	for i in range(0, len(text[1])):
		b += (text[1][i][1])**2
			
	denominator = a**0.5 * b**0.5

	return numerator/denominator
	
	
	
	
if __name__ == '__main__':
	start1 = time()
	with open('number.txt', 'rb') as pickle_file:
		a = pickle.load(pickle_file)
		print('They are : ' + str(cos(a)) + ' apart.')
	print('Time taken: {}'.format(time() - start1))
