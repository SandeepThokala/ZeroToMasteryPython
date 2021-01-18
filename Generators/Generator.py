def genf(num):
	for i in range(num):
		yield i

i = genf(100)
next(i)
print(next(i))

print('=' * 30)

from time import time
def performance(fn):
	def wrap(*args, **kwargs):
		t1 = time()
		fn(*args, **kwargs)
		t2 = time()
		print(f'took {t2 - t1}')
	return wrap()

@performance
def huge1():
	for i in range(9999999):
		i*5

@performance
def huge2():
	list(i*5 for i in range(9999999))

print('=' * 30)

