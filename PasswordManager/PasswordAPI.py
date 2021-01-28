import requests

url1 = 'https://api.pwnedpasswords.com/range/' + 'password123' 
res1 = requests.get(url1)
url2 = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res2 = requests.get(url2)
print(res1) #<Response [400]> (400 not good)
print(res2) #<Response [200]> (200 good)
