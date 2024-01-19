from datetime import datetime
from instagrapi import Client
from account import Account

account = Account()
USERNAME = account.get_account_id()
PASSWORD = account.get_account_password()


cl = Client()
cl.login(USERNAME, PASSWORD)

# medias = cl.hashtag_medias_top("진자림", amount=30)
# for media in medias:
#     print(media.dict())
# print(len(medias))

# followers = cl.user_followers(cl.user_id).keys()
# print(followers)

followings = cl.user_following(cl.user_id)
ids = []
for user_id in followings.keys():
    print(user_id)
    print(followings[user_id])
    print(followings[user_id].username)
    print("\n")
    # ids.append(user_id)
    cl.direct_send("How are you?", user_ids=[user_id])

# user_ids를 배열로 넘기면 그룹 메세지로 보내짐
# cl.direct_send("How are you?", user_ids=ids)
# cl.user_follow("8173009078")
