import tweepy
import pandas as pd
import csv
import twitter_credentials as tc
import json

auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
# try:
#     csvFile = open('../../Desktop/ua.csv', 'a', encoding='utf-8')
# except FileNotFoundError as e:
#     print("File not found error message : {}".format(e.strerror))

# csvWriter = csv.writer(csvFile)

tweets = tweepy.Cursor(api.search, q="iphone", lang="en", since="2019-04-10").items(100)

for tweet in tweets:
    # x = tweepy.models.Place(tweet.place)
    # print(tweet.place)
    # print(type(tweet.place))
    if tweet.place != None:
        print (tweet.place.country + " " + tweet.place.full_name)

# for tweet in tweets:
#     x = tweet.created_at
#     y = tweet.text
#     csvWriter.writerow([x, y])
#
# csvFile.close()