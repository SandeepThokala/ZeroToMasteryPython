import sys
from random import randint
a, b = min(int(sys.argv[1]), int(sys.argv[2])), max(int(sys.argv[1]), int(sys.argv[2]))
rn = randint(a, b + 1)
print(f'Guess a number between {a} and {b} including both: ', end = '')
while True:
	try:
		guess = int(input())	
		if (a <= guess <= b):
			if guess == rn:
				print('You are a genius')
				break
			else:
				print('Lol broo, just missu..., guess again: ', end = '')
		else:
			print(f'I SAID..!!,  BETWEEN {a} AND {b}..!!')
			print('Now, guess again..: ', end = '')
			continue
	except:
		print('I SAID..!!, A NUMBER..!!')		
		print('Now, guess again..: ', end = '')