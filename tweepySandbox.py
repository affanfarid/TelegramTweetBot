import tweepy
import configparser as cfg

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

wojtweets = api.user_timeline("wojespn", count=1)
for tweet in wojtweets:
    print(tweet.text)
    print(tweet.user.id)

#print(wojtweets)