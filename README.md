#Telegram Tweet Bot

###This is a Telegram Bot framework which streams in live tweets and instantly sends them as a message to your Telegram groups/users

##How to Run:
1. Set up config.cfg with your API Keys
2. Include all your Telegram Groups in botRunner.py
    -Put all group/user chat IDs in telegramGroupIDList
    -(Telegram does not yet support broadcasting via bots, so we have to include all groups/users :( )
    -To get the group/user chat IDs, add your bot to the group/user chat, then visit `https://api.telegram.org/bot [INSERT YOUR TELEGRAM BOT API KEY] /getUpdates`
    -Find the ID number (should include the "-") via `[result][0][message][chat][id]` in the JSON

3. Set all your Twitter stream filter rules in botRunner.py
    -Include and object for each filter
    -For more details on how to craft filters, reference the [Twitter API](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule)

4. Run botRunner.py

###For any questions, feel free to contact me:
Twitter: @AffanFarid3
Telegram: @Affav