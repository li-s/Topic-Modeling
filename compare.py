from xml1 import myfunc
from pprint import pprint
from time import time


def compare(file, length, func1):
	start1 = time()
	val1 = func1(length, file)
	print('My function timing: {}'.format(time() - start1))

	with open('./data/extracted_texts.txt', 'w') as fout:
		pprint(val1, stream = fout)


if __name__ == '__main__':
	a = "/home/li/Downloads/enwiki-latest-pages-articles.xml.bz2"
	b = input('Enter number of texts: ')
	compare(a, int(b) , myfunc)
