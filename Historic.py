import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = ('OdhLfB9zsDjPzqvENVToLHYA1')
consumer_secret = ('0KnTZHm5AilBunoH3diyRP8vk9IOKOZvPVpidK0H3rg1T0Bv29')
access_token = ('208239662-ve8CfcOV8Vy0eAIrIlMMhN6GKvbFEs7gIJw9oZal')
access_secret = ('1x1uLHpvmWLdoIS6WRlIZBB4UZfOnUK43rgb9bUD9UM54')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('1.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#python",count=100,
                           lang="en",
                           since="2017-04-03").items():


    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
