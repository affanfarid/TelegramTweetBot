import tweepy
import configparser as cfg
import json
import string

config = "config.cfg"
parser = cfg.ConfigParser()
parser.read(config)

telegramToken = parser.get('creds', 'telegramToken')
consumer_key = parser.get('creds', 'twitterAPIkey')
consumer_secret = parser.get('creds', 'twitterAPIsecret')
access_token = parser.get('creds', 'twitterAccessToken')
access_token_secret = parser.get('creds', 'twitterAccessTokenSecret')


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret )


api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# wojtweets = api.user_timeline("cnn", count=1)
# for tweet in wojtweets:
#     print(tweet.text)
#     print(tweet.user.id)

#print(wojtweets)

x =  '{ "name":"John", "age":30, "city":"New York"}'

dumpy = '{ "data": {"author_id": "17106279","created_at": "2020-12-17T03:14:15.000Z","id": "1339408539933175809","text": "Bulls 124, Thunder 103\n\nCoby White 27 points\nZach LaVine 24 points\nPatrick Williams 13 points, 7 rebounds in 1st start"},"includes": {"users": [{"created_at": "2008-11-01T22:24:10.000Z","id": "17106279","name": "K.C. Johnson","username": "KCJHoop"}]},"matching_rules": [{"id": 1339408365148123145,"tag": null}]}'


dumpy = dumpy.replace('\n', '')
#print(dumpy)
y = json.loads(dumpy)

#print(y["data"]['text'])
print(y["includes"]["users"][0]["name"])