import requests
import json
import configparser as cfg
import tweepy

config = "config.cfg"
parser = cfg.ConfigParser()
parser.read(config)

telegramToken = parser.get('creds', 'telegramToken')

telegramurl = "https://api.telegram.org/bot{}/".format(telegramToken)

url1 = "https://api.telegram.org/bot1460594069:AAFJfQ7oPGeHFU8cOud8snZBytQgknxwKyY/sendMessage?chat_id=167025498&text=ligma"
#response = requests.post(url1)

payload = {"chat_id": "167025498", "text": "lakersin4"}
payload2 = {"chat_id": "-419068391", "text": "test3"}
response = requests.post(telegramurl+ "sendMessage", data=payload2)


print(response)
print(response.url)