import requests
import json
import configparser as cfg

class telegram_TweetBot():
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        
    def get_updates(self, offset=None):
        #check for an update every 100 sec
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
        #only if the message is not empty, ping the telegram api with the url
        if msg is not None:
            requests.get(url)

    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')