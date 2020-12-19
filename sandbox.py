import requests
import json
import configparser as cfg
import tweepy
from telegramBot import TelegramBot
from twitterConnection import TwitterConnection
from twitterStreamListener import TwitterStreamListener
from twitterStreamConnection import TwitterConnection

# config = "config.cfg"
# parser = cfg.ConfigParser()
# parser.read(config)

# telegramToken = parser.get('creds', 'telegramToken')

# telegramurl = "https://api.telegram.org/bot{}/".format(telegramToken)

# url1 = "https://api.telegram.org/bot1460594069:AAFJfQ7oPGeHFU8cOud8snZBytQgknxwKyY/sendMessage?chat_id=167025498&text=ligma"
# #response = requests.post(url1)

# payload = {"chat_id": "167025498", "text": "lakersin4"}
# payload2 = {"chat_id": "-419068391", "text": "test3"}
# response = requests.post(telegramurl+ "sendMessage", data=payload2)


# print(response)
# print(response.url)


# connection = TwitterConnection("config.cfg")
bot = TelegramBot("config.cfg")
gID = "-419068391"


# tweets = connection.api.user_timeline("ShamsCharania", count=1)
# for tweet in tweets:
#     tweetUrl = "https://twitter.com/{}/status/{}".format(tweet.user.screen_name, tweet.id)
#     msg = "[@{}] {}: {} {}".format(tweet.user.screen_name, tweet.user.name, tweet.text, tweetUrl)

#     bot.sendMessage("-419068391", msg)



###
# followList = ["wojespn","ShamsCharania","Lakers", "CNN","BleacherReport" ]
# # affan "1270236623486287873"
# # wojespn 50323173
# # cnn 759251

# myStreamListener = TwitterStreamListener(bot, gID)
# myStream = tweepy.Stream(auth = connection.api.auth, listener=TwitterStreamListener(bot,gID))
# #myStream.filter(track=['Lakers'])
# #myStream.filter(follow=followList )
# myStream.filter(follow=["759251"] )

#-------------------------

# stream_url = "https://api.twitter.com/labs/1/tweets/stream/filter?format=detailed"
# rules_url = "https://api.twitter.com/labs/1/tweets/stream/filter/rules"
# consumer_key = parser.get('creds', "twitterAPIkey")
# consumer_secret = parser.get('creds', "twitterAPIsecret")

# def get_bearer_token():
#     response = requests.post(
#         "https://api.twitter.com/oauth2/token",
#         auth=(consumer_key, consumer_secret),
#         data={"grant_type": "client_credentials"}
#     )

#     if response.status_code is not 200:
#         print("cant get a bearer token. {} : {}".format(response.status_code, response.text) )

#     body = response.json()
#     return body['access_token']

# def create_rule():
#     payload = {
#         "add": [
#             {
#                 "value": "context:123.1220701888179359745  lang:en -is:retweet", "tag": "covid"
#             }
#         ]
#     }

#     response = requests.post("GET",rules_url,
#                             headers={"Authorization": "Bearer {}".format(
#                                     get_bearer_token()) }, json=payload)
    

#     if response.status_code == 201:
#         print("Response: {}".format(response.text))
#     else:
#         print("Cannot create rules. {} : {}".format(response.status_code, response.text))


# #print(get_bearer_token())
# create_rule()

#----------------------------
gID = ["-419068391"]

rules = [
        {"value": "from:wojespn -is:retweet -has:links"},
        {"value": "from:TheSteinLine -is:retweet -has:links"},
        {"value": "from:ShamsCharania -is:retweet -has:links"},
        {"value": "from:ChrisBHaynes -is:retweet -has:links"},
        {"value": "from:KCJHoop -is:retweet"},
        {"value": "from:affanfarid3 -is:retweet -has:links"}
    ]

tc = TwitterConnection("config.cfg",bot, gID, rules)
