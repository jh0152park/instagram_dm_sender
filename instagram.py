from instagrapi import Client


class Instagram:
    def __init__(self, username, password):
        self.cl = Client()
        self.username = username
        self.password = password

        self.cl.login(self.username, self.password)

    def get_hashtag_medias_top(self, tag: str, num: int) -> list:
        return self.cl.hashtag_medias_top(tag, num)

    # 나를 팔로우 하는 사람들
    def get_my_followers(self) -> dict:
        return self.cl.user_followers(self.cl.user_id)

    # 내가 팔로잉 하는 사람들
    def get_my_followings(self) -> dict:
        return self.cl.user_following(self.cl.user_id)

    def send_single_dm(self, message: str, receiver_id: str) -> None:
        self.cl.direct_send(message, user_ids=[receiver_id])

    def send_group_dm(self, message: str, reveiver_id_list: list = []) -> None:
        self.cl.direct_send(message, user_ids=[reveiver_id_list])

    def follow(self, user_id: str) -> None:
        self.cl.user_follow(user_id)

    def unfollow(self, user_id: str) -> None:
        self.cl.user_unfollow(user_id)
