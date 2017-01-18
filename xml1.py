import xml.etree.cElementTree as etree
import bz2
from pprint import pprint


#enwiki-latest-pages-articles.xml

#context = etree.iterparse('enwiki-latest-pages-articles.xml', events=('start', 'end'))

#context = iter(context)

#event, root = context.__next__()


def myfunc(length, file):
	i = 0
	res = []
	for event, elem in etree.iterparse(bz2.BZ2File(file), events=('start', 'end', 'start-ns')):
		if event == 'start' and i < length:
			continue
		
		elif event == 'end' and i < length:
			if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
				if len(elem.text) > 200:
					i += 1
					res.append(elem.text)
					res.append('abcdefghijklmnopqrstuvwxyzzz')
					#pprint(elem.text)
		elif i >= length :
			return (res)

if __name__ == '__main__':
	val = myfunc(2, "/home/li/Downloads/enwiki-latest-pages-articles.xml.bz2")
	pprint(val)
