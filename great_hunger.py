import tweepy, time, sys, os

CONSUMER_KEY = 'key'
CONSUMER_SECRET = 'secret'
ACCESS_KEY = 'key'
ACCESS_SECRET = 'secret'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('text.txt','r')
text=filename.readlines()
filename.close()

filename=open('counter.save','r')
count=int(filename.read())
filename.close()

api.update_status(status=text[count])

count += 1
print(count)

filename=open('counter.save','w')
filename.write(str(count))
filename.close()
