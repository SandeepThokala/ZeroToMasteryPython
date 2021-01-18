def fib(n):
	a = 0
	b = 1
	t = 0
	l = [0,1]
	for i in range(n):
		t = a+b
		a = b
		b = t
	yield a
'''	
for ii in fib(0):
	print(ii)		
	'''

def golden_ratio(n):
	for k in range(2, n):
		for i in fib(k):
			for j in fib(k-1):
				print(f'fib({k}):    {i}, fib({k-1}):    {j}')
			print('golden ratio: ', i/j , '\n')


golden_ratio(42)

