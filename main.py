import time
from account import Account
from instagram import Instagram

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m",
}

account = Account()
USERNAME = account.get_account_id()
PASSWORD = account.get_account_password()
influencers = account.get_influencers()

ig = Instagram(USERNAME, PASSWORD)
# followings = ig.get_my_followings()

# for user_id in followings:
#     fullname = followings[user_id].full_name
#     username = followings[user_id].username
#     print(f"{fullname} / {username} / {user_id}")


count = 1
print(colors["yellow"] + f"Start to follow influencers" + colors["reset"])
for influencer, id in influencers.items():
    try:
        print(
            "try following to "
            + colors["red"]
            + f"{influencer}"
            + colors["reset"]
            + f" [{count} / {len(influencers)}]"
        )
        ig.follow(id)
    except Exception as e:
        print(
            "can not following to " + colors["red"] + f"{influencer}" + colors["reset"]
        )
        print(e)
    count += 1
    time.sleep(5)

count = 1
print(colors["green"] + f"Start to unfollow influencers" + colors["reset"])
for influencer, id in influencers.items():
    try:
        print(
            "try unfollowing to "
            + colors["red"]
            + f"{influencer}"
            + colors["reset"]
            + f" [{count} / {len(influencers)}]"
        )
        ig.unfollow(id)
    except Exception as e:
        print(
            "can not unfollowing to "
            + colors["red"]
            + f"{influencer}"
            + colors["reset"]
        )
        print(e)
    count += 1
    time.sleep(5)
