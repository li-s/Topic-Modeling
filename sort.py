from pprint import pprint

def getkey(item):
	return int(item[0])

with open('./data/intermediate_doc.txt', 'w') as w:
	with open('./data/g_format_doc.txt', 'r') as read:
		b = ''.join(read)
		remove = ['']
		texts = [text for text in b.split('\n') if text not in remove]
	
		document = []
		for i in range(0, len(texts)):
			a = texts[i].split()
			document.append(a)
		texts = document
				
		texts = sorted(texts, key = getkey)
#		pprint(texts, stream = w)

		for i in range(len(texts)):
			w.write(str(texts[i][0]) + ' ' + str(texts[i][1]) + ' '+ str(texts[i][2])+'\n')
