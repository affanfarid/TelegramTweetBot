import requests
import json
import configparser as cfg
import tweepy
from telegramBot import TelegramBot
from twitterConnection import TwitterConnection


#override tweepy.StreamListener to add logic to on_status
class TwitterStreamListener(tweepy.StreamListener):
    def __init__(self, bot, telegramGroupID):
        super().__init__()
        self.bot = bot
        self.telegramGroupID = telegramGroupID

    def on_status(self, status):
        print(status.text)

        tweet = status
        tweetUrl = "https://twitter.com/{}/status/{}".format(tweet.user.screen_name, tweet.id)
        msg = "[@{}] {}: {} {}".format(tweet.user.screen_name, tweet.user.name, tweet.text, tweetUrl)

        self.bot.sendMessage(self.telegramGroupID, msg)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            print("Disconnected Stream: Error {}".format(status_code))
            return False

# gID = "-419068391"
# bot = TelegramBot("config.cfg")

# myStreamListener = TwitterStreamListener(bot, gID)
# myStream = tweepy.Stream(auth = api.auth, listener=TwitterStreamListener(bot,gID))
# #myStream.filter(track=['python'])
# myStream.filter(follow=['wojespn'])
