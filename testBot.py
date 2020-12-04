import requests
import random

url = "https://api.telegram.org/bot1460594069:AAFJfQ7oPGeHFU8cOud8snZBytQgknxwKyY/"

def getChatID(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def getMessageText(update):
    message_text = update["message"]["text"]
    return message_text

#function that gets last update
def lastUpdate(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]

    totalUpdates = len(result)-1
    #gets last recorded message update
    return result[totalUpdates]

#function that sends message from bot to user
def sendMessage(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url+ "sendMessage", data=params)
    return response

#main function for navigation or replying back
def main():
    update_id = lastUpdate(url)["update_id"]
    while True:
        print("cycle")
        update = lastUpdate(url)
        if update_id == update["update_id"]:
            msgText = getMessageText(update).lower()
            if msgText == "hi" or msgText == "hello":
                sendMessage(getChatID(update), "Hello welcome to our bot. Type 'play' to roll the dice")
            elif msgText == "play":
                diceRoll = random.randint(1,6)
                sendMessage(getChatID(update), "You rolled a {}".format(diceRoll) )
            else:
                sendMessage(getChatID(update), "i didnt understand, sorry bro")
            update_id += 1

print("start")
main()
