import json


class Account:
    def __init__(self):
        self.id = ""
        self.password = ""
        self.read_account_json()

    def read_account_json(self):
        with open("account.json") as f:
            json_data = json.load(f)
            self.id = json_data.get("id")
            self.password = json_data.get("password")

    def get_account_id(self):
        return self.id

    def get_account_password(self):
        return self.password
