import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

txtinfo = []
for line in open('twitcred.txt'):
	line1 = line.rstrip('\n')
	txtinfo.append(line1)

consumer_key = txtinfo[0]
consumer_secret = txtinfo[1]
access_token_key = txtinfo[2]
access_token_secret = txtinfo[3]

start_time = time.time()
keyword_list = ['iPhone 6S']

#Listener Class Override
class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
 
	def on_data(self, data):
 
		while (time.time() - self.time) < self.limit:
 
			try:
 
				saveFile = open('iphone6s_tweets.json', 'a')
				saveFile.write(data)
				saveFile.write('\n')
				saveFile.close()
 
				return True
 
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		exit()
 
	def on_error(self, status):
 
		print statuses

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit=20))
twitterStream.filter(track=keyword_list,languages=['en'])