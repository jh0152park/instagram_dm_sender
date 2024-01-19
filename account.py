import json


class Account:
    def __init__(self):
        self.id = ""
        self.password = ""
        self.influencers = {}
        self.read_account_json()
        self.read_influencer_json()

    def read_account_json(self):
        with open("account.json") as f:
            json_data = json.load(f)
            self.id = json_data.get("id")
            self.password = json_data.get("password")

    def read_influencer_json(self):
        with open("influencer.json") as f:
            json_data = json.load(f)
            for influencer in json_data.keys():
                self.influencers[influencer] = json_data[influencer]

    def get_account_id(self):
        return self.id

    def get_account_password(self):
        return self.password

    def get_influencers(self):
        return self.influencers
