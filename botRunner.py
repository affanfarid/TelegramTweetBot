from telegramBot import TelegramBot
from twitterStreamConnection import TwitterConnection


bot = TelegramBot("config.cfg")

telegramGroupIDList = ["-419068391", "-1001082696712"]

rules = [
        {"value": "from:wojespn -is:retweet -has:links"},
        {"value": "from:TheSteinLine -is:retweet -has:links"},
        {"value": "from:ShamsCharania -is:retweet -has:links"},
        {"value": "from:ChrisBHaynes -is:retweet -has:links"},
        {"value": "from:KCJHoop -is:retweet"},
        {"value": "from:affanfarid3 -is:retweet -has:links"}
    ]

tc = TwitterConnection("config.cfg",bot, telegramGroupIDList, rules)