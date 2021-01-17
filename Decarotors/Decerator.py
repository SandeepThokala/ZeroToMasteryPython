def decorator(func):
	def wrap():
		print('************')
		func()
		print('************')
	return wrap

@decorator
def hi():
	print('Hello raa')

print(hi())

print('=====================================================')

def hello():
	print('hi raa ')

decorator(hello)()

print('=====================================================')

from time import time 

def performance(func):
	def wrap(*args, **kwargs):
		t1 = time()
		print(f't1:{t1}')
		func(*args, **kwargs)
		t2 = time()
		print(f't2:{t2}')
		print(f'took {t2 - t1} s')
	return wrap()


@performance
def huge():
	for i in range(9999999):
		i*5

