'''
my_file = open('file.txt')
print(my_file.readlines())
#my_file.seek(0)
#print(my_file.read())
#my_file.seek(0)
#print(my_file.read())
#my_file.seek(0)
my_file.close()
'''

with open('C:\\Users\\sande\\Desktop\\Deepu\\RandomGame.py', mode = 'r') as my_file:
	print(my_file.read())

with open(r'C:\Users\sande\Desktop\Deepu\ZTM\file.txt', mode = 'w') as tled:
	tled.write('Hi bro, I\'m Sandeep Thokala and I\'m going to be the hokage one day. Believe it..!!!.')
	
