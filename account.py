import json


class Account:
    def __init__(self):
        self.id = ""
        self.password = ""

    def read_account_json(self):
        with open("account.json") as f:
            json_data = json.load(f)
            print(json_data.get("id"))
            print(json_data.get("password"))
