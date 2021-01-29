import tweepy

auth = tweepy.OAuthHandler('BitpqyQlEGDaLYfj4VOCEiHz5', '4tE7FaMVEhnIQYPub4kJxZBS3LRyBa7OjHGtfeIlma2vSkSIRK')
auth.set_access_token('3836032333-f39jEii9qOl9m1hBSrH24pLctZ2912cY3eNH3BX', 'yAzeUcAFhEJaX64BE3nAKADDnnHJUw0u14q7JJfsCqp1g')

api = tweepy.API(auth)

'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
'''

user = api.me()

print(user.name, user.screen_name, f'no. of followers: {user.followers_count}', sep = '\n')
#Sandeep Thokala
#sandeep_thokala
#no. of followers: 27