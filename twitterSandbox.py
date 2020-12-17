import requests
import os
import json
import configparser as cfg
from telegramBot import TelegramBot

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


config = "config.cfg"
parser = cfg.ConfigParser()
parser.read(config)

consumer_key = parser.get('creds', "twitterAPIkey")
consumer_secret = parser.get('creds', "twitterAPIsecret")

bot = TelegramBot("config.cfg")
telegramGroupID = "-419068391"

def get_bearer_token():
    response = requests.post(
        "https://api.twitter.com/oauth2/token",
        auth=(consumer_key, consumer_secret),
        data={"grant_type": "client_credentials"}
    )

    if response.status_code is not 200:
        print("cant get a bearer token. {} : {}".format(response.status_code, response.text) )

    body = response.json()
    return body['access_token']


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def get_rules(headers, bearer_token):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(headers, bearer_token, rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(headers, delete, bearer_token):
    # You can adjust the rules if needed
    sample_rules = [
        # {"value": "dog has:images", "tag": "dog pictures"},
        # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
        #{"value": "dog has:images", "tag": "dog pictures"},
        {"value": "from:wojespn -is:retweet -has:links"},
        {"value": "from:TheSteinLine -is:retweet -has:links"},
        {"value": "from:ShamsCharania -is:retweet -has:links"},
        {"value": "from:ChrisBHaynes -is:retweet -has:links"},
        {"value": "from:KCJHoop -is:retweet"},
        {"value": "from:affanfarid3 -is:retweet -has:links"}
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(headers, set, bearer_token):
    newUrl = "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at"
    pastUrl = "https://api.twitter.com/2/tweets/search/stream"

    response = requests.get(
        newUrl, headers=headers, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            #line = response_line.replace('\n', '')

            json_response = json.loads(response_line)
            
            tweet = json_response
            # json_response = json_response.replace('\n', '')
            # tweet = json.loads(json_response)
            #tweet = json.loads(line)


            # tweet = status
            # tweetUrl = "https://twitter.com/{}/status/{}".format(tweet.user.screen_name, tweet.id)
            # msg = "[@{}] {}: {} {}".format(tweet.user.screen_name, tweet.user.name, tweet.text, tweetUrl)

            tweetText = tweet["data"]["text"]
            tweetName = tweet["includes"]["users"][0]["name"]
            tweetAt = tweet["includes"]["users"][0]["username"]
            tweetID = tweet["data"]["id"]

            tweetUrl = "https://twitter.com/{}/status/{}".format(tweetAt, tweetID)
            msg = "[@{}] {}: {} {}".format(tweetAt, tweetName, tweetText, tweetUrl)


            #msg = json.dumps(json_response, indent=4, sort_keys=True)

            # print("NAME: {}".format(msg["includes"]["users"]["name"]))
            # print("TEXT: {}".format(msg["data"]["text"]))

            #msg = json.dumps(json_response, indent=4, sort_keys=True)
            bot.sendMessage(telegramGroupID, msg)
            
            #print(json.dumps(json_response, indent=4, sort_keys=True))
            print(json.dumps(tweet, indent=4, sort_keys=True))
            print(msg)


def main():
    bearer_token = get_bearer_token()
    headers = create_headers(bearer_token)
    rules = get_rules(headers, bearer_token)
    deleteRules = delete_all_rules(headers, bearer_token, rules)
    setRules = set_rules(headers, deleteRules, bearer_token)
    get_stream(headers, setRules, bearer_token)


if __name__ == "__main__":
    main()