import pickle
from time import time

def identify(text):
	all_positions = []
	for i in range(len(text)):
		if len(text[i]) <= 8:
			all_positions.append(i)
	print(text[582])
	return all_positions
	
def select():
	return 1
	
	return None
if __name__ == '__main__':
	start1 = time()
	with open('./data/raw_pruned_texts(byte).txt', 'rb') as b:
		read = pickle.load(b)
		identify(read)
	print('Program ran for: {}'.format(time()-start1))
