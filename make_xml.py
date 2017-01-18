import xml.etree.cElementTree as etree
from pprint import pprint

def make_xml(length):
	i = 0
	for event, elem in etree.iterparse('../doc_similarity/enwiki-latest-pages-articles.xml', events=('end', )):
	
		try:
			if i < length:
				if event == 'end' and \
					elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text' and \
					len(elem.text) > 200:

					i += 1
					yield elem.text
				
			else:
				break
		except:
			pass
		elem.clear()
			
			
if __name__ == '__main__':
	a = int(input('Number of texts: '))
	b = int(input('Step seperation: '))
	c = a*b
	
	root = etree.Element('texts')
	
	for i, t in enumerate(make_xml(c)):
		if i % b == 0:
			print(i/b)
			doc = etree.SubElement(root, 'text')
			doc.text = t
	tree = etree.ElementTree(root)
	tree.write('./data/list_of_texts.xml')
	
	
	
	
	
#	root = etree.Element('texts')
#	tree = etree.ElementTree(root)
#	tree.write('./data/list_of_texts.xml')
#	
#	tree = xml.parse('./data/list_of_texts.xml')
#	xmlRoot = tree.getroot()
#	
#	for i, t in enumerate(make_xml(c)):

#		if i % int(b) == 0:
#			print(i/int(b))
#			doc = etree.SubElement(root, 'text')
#			doc.text = t
#	tree.write('./data/list_of_texts.xml')
