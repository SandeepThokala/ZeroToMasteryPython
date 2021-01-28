import requests
import hashlib
import sys

#code for generating hash version of password
#hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

#function for counting no. of times a pw was found
def read_res(response, tail):
	for hash1, count in (i.split(':') for i in response.text.splitlines()):
		if hash1 == tail:
			return count
	return 0

#function for running pw api url
def request_api(query_char):
	sha1pw = hashlib.sha1(query_char.encode('utf-8')).hexdigest().upper()
	url = 'https://api.pwnedpasswords.com/range/' + sha1pw[:5]
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error: {res.status_code}, Not Valid')
	return read_res(res, sha1pw[5:])

#main function
def main(args):
	for password in args:
		count = request_api(password)
		if count:
			print(f'Password \'{password}\' was found {count} times..!')
		else:
			print('good')
	return 'done..!'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))