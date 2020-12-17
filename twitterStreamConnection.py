import requests
import os
import json
import configparser as cfg

class TwitterConnection():
    def __init__(self, config, bot, telegramGroupID):
        self.APIKey = self.read_token_from_config_file(config,"twitterAPIkey")
        self.APISecret = self.read_token_from_config_file(config,"twitterAPIsecret")
        
        self.bot = bot
        self.telegramGroupID = telegramGroupID

        self.bearerToken = self.get_bearer_token()
        self.headers = self.create_headers(self.bearerToken)
        self.rules = self.get_rules(self.headers, self.bearerToken)
        self.deleteRules = self.delete_all_rules(self.headers, self.bearerToken, self.rules)
        self.setRules =  self.set_rules(self.headers, self.deleteRules, self.bearerToken)




        # bearer_token = get_bearer_token()
        # headers = create_headers(bearer_token)
        # rules = get_rules(headers, bearer_token)
        # deleteRules = delete_all_rules(headers, bearer_token, rules)
        # setRules = set_rules(headers, deleteRules, bearer_token)
        # get_stream(headers, setRules, bearer_token)
    
    def read_token_from_config_file(self, config, tokenName):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', tokenName)

    def get_bearer_token(self):
        response = requests.post(
            "https://api.twitter.com/oauth2/token",
            auth=(self.APIKey, self.APISecret),
            data={"grant_type": "client_credentials"}
        )

        if response.status_code is not 200:
            print("cant get a bearer token. {} : {}".format(response.status_code, response.text) )

        body = response.json()
        return body['access_token']

    def create_headers(self, bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers
    
#-------------------------------------------------

    def get_rules(self,headers, bearer_token):
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
            )
        print(json.dumps(response.json()))
        return response.json()


    def delete_all_rules(self, headers, bearer_token, rules):
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


    def set_rules(self, headers, delete, bearer_token):
        # You can adjust the rules if needed
        sample_rules = [
            # {"value": "dog has:images", "tag": "dog pictures"},
            # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
            #{"value": "dog has:images", "tag": "dog pictures"},
            {"value": "from:wojespn -is:retweet -has:links"}
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


    def get_stream(self, headers, set, bearer_token):
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
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
                json_response = json.loads(response_line)
                print(json.dumps(json_response, indent=4, sort_keys=True))