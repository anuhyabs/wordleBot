#getTweets.py

"""
Created on Sat Mar  5 13:43:59 2022
Name: Twitter Data for Wordle
Description: Setting up dataset of tweets on Wordle
"""
import tweepy 
import pytz
from datetime import datetime
from twitterKeys import twitterKeys
import pandas as pd
import re

keys = twitterKeys()
twitter_api_key = keys.get_keys("twitter_api_key")
twitter_api_secret = keys.get_keys("twitter_api_secret")
auth = tweepy.AppAuthHandler(twitter_api_key, twitter_api_secret)
api = tweepy.API(auth)

wordle_start = pytz.timezone("US/Pacific").localize(datetime(2021, 6, 19))
now = pytz.utc.localize(datetime.now()).astimezone(pytz.timezone("US/Pacific"))

wordle_id = (now-wordle_start).days
print("Today's wordle_id is: %d (%s)" % (wordle_id, now.strftime("%Y-%m-%d %H:%M PT")))

wordle_tweets = []
def is_valid_wordle_tweet(tweet, wordle_id): 
    text = (tweet.replace("Y", "y").replace("🟩", "Y")
                 .replace("M", "m").replace("🟨", "M")
                 .replace("N", "n").replace("⬛", "N").replace("⬜", "N"))
    for i in range(wordle_id-20, wordle_id+20):
        if i==wordle_id:
            continue
        if str(i) in text:
            return False
    
    if len(re.findall("Wordle %d" % wordle_id, text)) != 1:
        return False

    if re.match("Wordle %d [2-6]/6\n\n[YMN]{5}\n" % wordle_id, text) is None:
        return False
    return True

cursor = tweepy.Cursor(api.search_tweets, q="wordle %d" % wordle_id)
tweets = list(cursor.items(5000))
for tweet in tweets:
    wordle_tweets.append((wordle_id, tweet.text))

print("Pulled %d tweets for wordle %d" % (len(wordle_tweets), wordle_id))

tweets_df = pd.DataFrame([tweet for tweet in wordle_tweets if is_valid_wordle_tweet(tweet[1], tweet[0])],
                             columns=["wordle_id", "tweet_text"])
tweets_df.to_csv("./data/tweets.csv")

