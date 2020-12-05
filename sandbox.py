import requests
import json
import configparser as cfg
import tweepy
from telegramBot import TelegramBot
from twitterConnection import TwitterConnection
from twitterStreamListener import TwitterStreamListener

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

connection = TwitterConnection("config.cfg")
bot = TelegramBot("config.cfg")
gID = "-419068391"


# tweets = connection.api.user_timeline("ShamsCharania", count=1)
# for tweet in tweets:
#     tweetUrl = "https://twitter.com/{}/status/{}".format(tweet.user.screen_name, tweet.id)
#     msg = "[@{}] {}: {} {}".format(tweet.user.screen_name, tweet.user.name, tweet.text, tweetUrl)

#     bot.sendMessage("-419068391", msg)



###
followList = ["wojespn","ShamsCharania","Lakers", "CNN","BleacherReport" ]

myStreamListener = TwitterStreamListener(bot, gID)
myStream = tweepy.Stream(auth = connection.api.auth, listener=TwitterStreamListener(bot,gID))
#myStream.filter(track=['Lakers'])
#myStream.filter(follow=followList )
myStream.filter(follow=["@cnn","cnn"] )
