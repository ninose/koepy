import requests


class KoeClient():
    headers = {
        'User-Agent': 'S/3.8.4 (iPhone; iOS 14.3; Scale/2.00)',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'ja-JP;q=1',
        'Accept': 'application/json',
        'Accept': '*/*',
        'Accept-Language': 'ja-jp',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    host = "https://api.meetscom.com/"
    auth_token = None
    uid = None

    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.uid = auth_token[:7]

    def get_feed(self, count):
        params = (('auth_token', self.auth_token),
                  ('consistency', '1'),
                  ('currentTotal', '0'),
                  ('version', 'ios_3.8.4'),
                  ('count', count),)
        url = self.host + "api/feed_posts"
        return requests.get(url, headers=self.headers, params=params).json()

    def feed_like(self, feed_id):
        data = {
            'auth_token': self.auth_token,
            'feed_post_id': feed_id,
            'uid': self.uid,
            'version': 'ios_3.8.4'
        }
        url = self.host + "api/feed/feed_post_liked_user"
        return requests.post(url, headers=self.headers, data=data).json()

    def feed_comment(self, feed_id):
        data = {
            'auth_token': self.auth_token,
            'feed_post_id': feed_id,
            'text': '\u304A\u306F\u3088\uFF01\uFF01\uFF01',
            'uid': self.uid,
            'version': 'ios_3.8.4'
        }
        url = self.host + "api/feed/feed_post_comment"

        return requests.post(url, headers=self.headers, data=data).json()
