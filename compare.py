from xml1 import myfunc
from xml2 import standard
from control import myfunc1
from pprint import pprint
from time import time


def compare(file, length, func1, func2, func3):
	start1 = time()
	val1 = func1(length, file)
	print('My function timing: {}'.format(time() - start1))
	
	start2 = time()
	val2 = func2(length, file)
	print('Standard function timing: {}'.format(time() - start2))
	
	start3 = time()
	val3 = func3(length)
	print('Control function timing: {}'.format(time() - start3))

	with open('my.txt', 'w') as fout:
		pprint(val1, stream = fout)
#	with open('standard.txt', 'w') as a:
#		pprint(val2, stream = a)


if __name__ == '__main__':
	a = "/home/li/Downloads/enwiki-latest-pages-articles.xml.bz2"
	b = input('Enter number of texts: ')
	compare(a, int(b) , myfunc, standard, myfunc1)
