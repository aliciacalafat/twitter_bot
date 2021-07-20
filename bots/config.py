
#============================================================================
# Functionality in common for all the bots.                        02/01/2021
#============================================================================

import tweepy
import logging

logger = logging.getLogger()

def create_api():
	consumer_key = 'iuCiPMTjb6sixlSVuO9CLwmwd'
	consumer_secret = '9JsveKvn9yOyQ0YVm9HK1JseEb72T3ecFIFVUfpuupvY7Znfrb'
    access_token = '1345328204513501185-lgKjrdxLIHfPvidle8cLLj5AjG4nBF'
    access_token_secret = 'KoS7siPvxeWO38UQlcCtohba9G8jLuQR28SXdKnrQM8Vt'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
          wait_on_rate_limit_notify=True) # This True statements makes Tweepy 
        # wait and print a message when the rate limit is exceeded
    try:
        api.verify_credentials() # To check that the credentials are valid.
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

#______________________________ Note _________________________________________

# If you rant to use environment variables, that means, to put
# in yout terminal the consumer key, etc outside this python, change 
# this script with:

# import os
# consumer_key = os.getenv("CONSUMER_KEY")
# consumer_secret = os.getenv("CONSUMER_SECRET")
# access_token = os.getenv("ACCESS_TOKEN")
# access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
