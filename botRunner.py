from telegramBot import TelegramBot
from twitterStreamConnection import TwitterConnection


bot = TelegramBot("config.cfg")
gID = ["-419068391"]

rules = [
        {"value": "from:wojespn -is:retweet -has:links"},
        {"value": "from:TheSteinLine -is:retweet -has:links"},
        {"value": "from:ShamsCharania -is:retweet -has:links"},
        {"value": "from:ChrisBHaynes -is:retweet -has:links"},
        {"value": "from:KCJHoop -is:retweet"},
        {"value": "from:affanfarid3 -is:retweet -has:links"}
    ]

tc = TwitterConnection("config.cfg",bot, gID, rules)