from pprint import pprint

def maker(a_text):
	b = ''.join(a_text)
	texts = [text for text in b.split('\n')]
	
	texts = ' '.join(texts)
	texts = texts.split('abcdefghijklmnopqrstuvwxyzzz')

	document = []
	for i in range(0, len(texts)-1):
		a = texts[i].split()
		document.append(a)
	texts = document	#makes a list with the lines in the previous txt as sub lists


	document = []
	
	i = 0
	while i <= len(texts):
		number = 0
		number = int(texts[i][2])
		
		if int(texts[i][0]) == int(texts[i+1][0]):
			number += int(texts[i+1][2])
			i+=1
			
		else:
			i+=1
			
		a = number
		appending = str(texts[i][0]) + '\t'+ str(texts[i][1]) +'\t' + str(number) +'\n'
		document.append(appending)
						
	return document
	#return res

if __name__ == '__main__':
	with open('./data/use_this_lda.txt', 'w') as w:
		with open('./data/g_format_doc.txt', 'r') as read:
			pprint(maker(read), stream = w)
