import tweepy
import time

auth = tweepy.OAuthHandler('BitpqyQlEGDaLYfj4VOCEiHz5',
	 '4tE7FaMVEhnIQYPub4kJxZBS3LRyBa7OjHGtfeIlma2vSkSIRK')

auth.set_access_token('3836032333-f39jEii9qOl9m1hBSrH24pLctZ2912cY3eNH3BX', 
	'yAzeUcAFhEJaX64BE3nAKADDnnHJUw0u14q7JJfsCqp1g')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
	try:
		while 1:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)
	except StopIteration:
		print('End')

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	if follower.name == 'Winfo Movies':
		follower.follow()


search = 'Python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break