import xml.etree.cElementTree as etree
import bz2
from pprint import pprint
from time import time

#enwiki-latest-pages-articles.xml

#context = etree.iterparse('enwiki-latest-pages-articles.xml', events=('start', 'end'))

#context = iter(context)

#event, root = context.__next__()


def myfunc(length, file):
	i = 0
	res = []
	seperation = 0
	for event, elem in etree.iterparse(bz2.BZ2File(file), events=('end',)):

		try:
			if i < length:
				if event == 'end' and \
					elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text' and \
					len(elem.text) > 200:

					if seperation < 300:
						seperation += 1

					else:
						i += 1
						res.append(elem.text)
						res.append('abcdefghijklmnopqrstuvwxyzzz')
						seperation = 0

			else:
				return(res)

		except:
			pass
		elem.clear()

if __name__ == '__main__':
	a = "/home/li/Downloads/enwiki-latest-pages-articles.xml.bz2"
	b = int(input('Enter number of texts: '))

	start1 = time()

	with open('../data/extracted_texts.txt', 'w') as fout:
		pprint(myfunc(b, a), stream  = fout)

	print('My function timing: {}'.format(time() - start1))
