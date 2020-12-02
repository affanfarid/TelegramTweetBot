import requests

url = "https://api.telegram.org/bot1460594069:AAFJfQ7oPGeHFU8cOud8snZBytQgknxwKyY/"

url1 = "https://api.telegram.org/bot1460594069:AAFJfQ7oPGeHFU8cOud8snZBytQgknxwKyY/sendMessage?chat_id=167025498&text=ligma"
#response = requests.post(url1)



payload = {"chat_id": "167025498", "text": "lakersin4"}
response = requests.post(url+ "sendMessage", data=payload)
print(response)
print(response.url)