import requests
import json
import configparser as cfg

class TelegramBot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config, 'telegramToken')
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    #need to fix??    
    def getUpdates(self, offset=None):
        #check for an update every 100 sec
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        r = requests.get(url)
        return json.loads(r.content)

    def sendMessage(self, chat_id, msg):
        #only if the message is not empty, ping the telegram api with the url
        if msg is not None:
            payload = {"chat_id": chat_id , "text": msg }
            response = requests.post(self.base+ "sendMessage", data=payload)
            return response
        

    def read_token_from_config_file(self, config, tokenName):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', tokenName)

