import xml.etree.cElementTree as etree
from pprint import pprint


def myfunc1(length):
	i = 0
	res = []
	for event, elem in etree.iterparse('enwiki-latest-pages-articles.xml', events=('start', 'end', 'start-ns')):
		if event == 'start' and i < length:
			continue
		
		elif event == 'end' and i < length:
			if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
				if len(elem.text) > 200:
					res.append(elem.text)
					#pprint(elem.text)
					elem.clear()
					i += 1
		elif i >= length :
			return res

if __name__ == '__main__':
	val = myfunc(1)
	pprint(val)
