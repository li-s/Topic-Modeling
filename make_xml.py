import xml.etree.cElementTree as etree
from pprint import pprint

def make_xml(length, step):
	i = 0
	counter = 0

	for event, elem in etree.iterparse('enwiki-latest-pages-articles.xml', events=('start', 'end', 'start-ns')):
		try:
			if event == 'start' and i < length:
				continue

			elif event == 'end' and i < length and counter != step:
				if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
						if len(elem.text) > 200:
								counter += 1

					
							
			elif event == 'end' and i < length and counter == step:
				if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
					if len(elem.text) > 200:			
						yield elem.text
						elem.clear()
						i += 1
						counter = 0
						
			elif i >= length:
				break
		except:
			continue
			
			
if __name__ == '__main__':
	a = input('Number of texts: ')
	b = input('Step seperation: ')
	
	root = etree.Element('texts')
	for i, t in enumerate(make_xml(int(a), int(b))):
		doc = etree.SubElement(root, 'text')
		doc.text = t
		if i % 100 == 0:
			print(i)
	
	tree = etree.ElementTree(root)
	tree.write('my_xml.xml')
