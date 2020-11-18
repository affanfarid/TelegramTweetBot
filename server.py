#from bot import telegram_TweetBot
from bot import telegram_TweetBot


bot = telegram_TweetBot("config.cfg")


def make_reply(msg):
    if msg is not None:
        reply = "Okay"
    return reply

update_id = None
while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    #error message
    if updates["ok"] == False:
        print('{}: {}'.format(updates["error_code"],updates["description"]))
        break
    updates = updates["result"]

    if updates:
        for item in updates:
            try:
                update_id = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply,from_)