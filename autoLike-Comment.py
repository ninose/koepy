import time

from koepy import KoeClient


def main():
    while True:
        process_count = 0
        try:
            #your token
            token = "your token"
            client = KoeClient(auth_token=token)

            feed = client.get_feed(100)
            feed_id_list = [i["id"] for i in feed["data"]["feed_posts"]]
            for feed_id in feed_id_list:
                like = client.feed_like(feed_id)
                comment = client.feed_comment(feed_id)
                process_count += 1
                print("like {} \n comment {} \n count {}".format(
                    like, comment, process_count))
            if process_count%100==0:
                continue
        except:
            print("エラーだよ＞＜")
            time.sleep(100)

if __name__ == "__main__":
    main()
