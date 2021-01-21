from translate import Translator

t = Translator(to_lang = 'ja')

with open(r'C:\Users\sande\Desktop\Deepu\ZTM\file.txt', mode = 'r') as tled:
	txt = t.translate(tled.read())
	#print(txt)
	with open(r'C:\Users\sande\Desktop\Deepu\ZTM\jafile.txt', mode = 'w') as tted:
		tted.write(txt)
