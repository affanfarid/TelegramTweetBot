import requests
import json
import configparser as cfg
import tweepy

class TwitterConnection():
    def __init__(self, config):
        self.APIKey = self.read_token_from_config_file(config,"twitterAPIkey")
        self.APISecret = self.read_token_from_config_file(config,"twitterAPIsecret")
        self.accessToken = self.read_token_from_config_file(config,"twitterAccessToken")
        self.accessTokenSecret = self.read_token_from_config_file(config,"twitterAccessTokenSecret")

        self.api = self.connectToAPI()

    def read_token_from_config_file(self, config, tokenName):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', tokenName)

    def connectToAPI(self):
        auth = tweepy.OAuthHandler(self.APIKey,self.APISecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret )
        api = tweepy.API(auth)
        return api





# wojtweets = connection.api.user_timeline("wojespn", count=1)
# for tweet in wojtweets:
#     print(tweet.text)