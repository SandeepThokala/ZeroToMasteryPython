# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorlem',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  	# code here
 	def wrap(*args, **kwargs):
 		if args[0]['valid']:
 			fn(*args, **kwargs)
 	return wrap

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)