
import tweepy
import time

# This lines will configure what you need to read and write data from twitter.
screen_name = 'bot_parasite'
consumer_key = 'iuCiPMTjb6sixlSVuO9CLwmwd'
consumer_secret = '9JsveKvn9yOyQ0YVm9HK1JseEb72T3ecFIFVUfpuupvY7Znfrb'
access_key = '1345328204513501185-lgKjrdxLIHfPvidle8cLLj5AjG4nBF'
access_secret = 'KoS7siPvxeWO38UQlcCtohba9G8jLuQR28SXdKnrQM8Vt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# To write and read data from twitter use this variable:
api = tweepy.API(auth)

#===============================================================================

# List of followers and make tweets mentioning everuone of them:
def mention_followers():
	followers = api.followers()

for follower in followers:
       api.update_status('Hello @' + follower.screen_name)
while True:
   mention_followers()
   time.sleep(3600) # Prevents Twitter from blocking the account for spam

#____________________________________________________________________________________

# Stop following who does not follow you.
followers = api.followers_ids(screen_name)
friends = api.friends_ids(screen_name)

for f in friends:
    if f not in followers:
        api.destroy_friendship(f)
        print ("He dejado de seguir a {0}".format(api.get_user(f).screen_name))
        time.sleep(3600)  

#____________________________________________________________________________________

# Follow who follows you.
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Acabo de seguir a ") 
    print (follower.screen_name)
    time.sleep(3600)  

#____________________________________________________________________________________

# Give automatic retweet by hashtag and automatic like by hastag.
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user =  api.me()

search = 'Marketing' 
lang = 'es'
nrTweets = 15

# Automatic retweet.
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('He dado Retweet')
        tweet.retweet()
        time.sleep(3600)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Automatic like.
for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:
        print('He dado Like')
        tweet.favorite()
        time.sleep(3600)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break






