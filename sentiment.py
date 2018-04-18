import tweepy
from textblob import TextBlob

consumer_key = 	'nRIt2p732I4MJ3Hf2T2IL1P4B'
consumer_secret = 'UaizTD7FJkI3qirhycyt0ZCcFbvfz0P1CrRXBnfwXP9QdTyFcy'
access_token = 	'238960624-q3ox2zeRTap8k1Nfz6tvzp4gUvpGH23AOuE8MQvs'
access_token_secret = 	'2UoKZkkrDLkIIkryyN8oqMAFBBN8TJ2LHaMgfxh5oeBwV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
   print(tweet.text)
   analysis = TextBlob(tweet.text)
   print(analysis.sentiment)
   print('')
