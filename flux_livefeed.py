import tweepy
import time
import json
import sys
import fileinput
import re
import cgi
import urllib2
import urllib
import html2text

#data = json.load(urllib2.urlopen('https://boiling-inferno-993.firebaseio.com/hashtag.json'))

form = cgi.FieldStorage()
searchterm = form.getvalue('searchbox')

auth = tweepy.OAuthHandler() # your twitter access tokens here
auth.set_access_token()
api = tweepy.API(auth)

words=[]
opener = urllib2.build_opener()
headers = {'User-Agent': 'Mozilla/5.0'}
response = open

def print_word_counts():
	f = open("/home/scott/bausCoin", 'w') # your directory here
        for word in words:
        	word = word.encode('utf-8')
        	f.write(word + "\n")
	f.close()
	
# livestream
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, tweet):
		text = tweet.text
		followers = tweet.user.followers_count
		timestamp = tweet.created_at
		location = tweet.user.location
                language = tweet.user.lang
                favorites = tweet.favorite_count
                # retweets = tweet.retweet_count
		parsed = text.split()
		print (timestamp, location, language, followers, favorites, text)
		print "\n"

		# could also pull links in tweets with something like url = entities.urls

		# for word in parsed:
		# 	if word.startswith("http"):
		# 	print word
		#		f = urllib2.Request(word, None, headers)
		#		html = urllib2.urlopen(f).read()
		#		print html2text.html2text(html) 

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=["bitcoin"])
