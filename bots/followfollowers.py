
#============================================================================
# This bot gets your list of followers from Twitter every minute and then 
# iterates through it to follow each user that you’re not already following.                        
#                                                                  02/01/2021
#============================================================================

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()

def main(): # Every minnute follow_followers() is called.
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()

#______________________________________________________________________________
# To run a bot.

# In your directory of the bot, activate python and this file.
# You can stop the bot using Ctrl-C.
