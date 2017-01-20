import bz2

#a = bz2.BZ2File('./data/list_of_texts_compressed.xml.bz2', 'wb')

#a.write()

with open('./data/list_of_texts_compressed.xml.bz2', 'wb') as A:
	with open('./data/list_of_texts.xml', 'rb') as B:
		for data in B:
			A.write(data)
