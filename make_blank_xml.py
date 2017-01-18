import xml.etree.cElementTree as etree

root = etree.Element('root')
for i in range(10000):
	doc = etree.SubElement(root, "test")
	
tree = etree.ElementTree(root)
tree.write('test.xml')
