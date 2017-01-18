import xml.etree.cElementTree as etree
from pprint import pprint

def make_xml(length):
	i = 0
	counter = 0
	for event, elem in etree.iterparse('../doc_similarity/enwiki-latest-pages-articles.xml', events=('end',)):
	
		try:
			if i < length:
				if event == 'end': 
					if elem.tag == '{http://www.mediawiki.org/xml/export-0.10/}text':
						if len(elem.text) > 200:
					
							#if counter != step:
								#counter += 1
								#elem.clear()
							
							#elif counter == step:
							i += 1
								#counter = 0
							yield elem.text
							elem.clear()
						
			elif i >= length:
				break
		except:
			continue
			
			
if __name__ == '__main__':
	a = input('Number of texts: ')
	b = input('Step seperation: ')
	
	c = int(a)*int(b)
	root = etree.Element('texts')
	for i, t in enumerate(make_xml(c)):
		doc = etree.SubElement(root, 'text')
		#doc.text = t
		if i % 300 == 0:
			print(i/300)
			doc.text = t
	tree = etree.ElementTree(root)
	tree.write('./data/list_of_texts.xml')
