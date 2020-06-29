import GetOldTweets3 as got
from datetime import datetime
import json
import uuid
# import re
from textblob import TextBlob
# import datetime as dt


# below for elasticsearch
def write_ndjson(filename, arr):
    with open(filename, 'a') as f:
        for json_line in arr:
            f.write(
                '{"index": {"_index": "tweets", "_type": "tweet"}}' + '\n')
            json.dump(json_line, f)
            f.write('\n')


# def remove_url(txt: str) -> str:
#     url_pattern = re.compile(r'https?://\S+|www\.\S+')
#     no_url = url_pattern.sub(r'', txt)

#     return no_url

def get_historical_tweets(query: str, start_date: str, end_date: str, top_only=True, max_tweets=1000):
    """
    start_date ex: 2020-06-01
    end_date ex: 2020-06-15
    """
    tweetCriteria = got.manager.TweetCriteria()\
                               .setQuerySearch(query)\
                               .setTopTweets(top_only)\
                               .setLang("en")\
                               .setSince("2020-06-01")\
                               .setUntil("2020-06-15")\
                               .setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    print(type(tweets))


if __name__ == "__main__":

    tweetCriteria = got.manager.TweetCriteria()\
                               .setQuerySearch('DACA')\
                               .setTopTweets(True)\
                               .setLang("en")\
                               .setSince("2020-06-01")\
                               .setUntil("2020-06-15")\
                               .setMaxTweets(7000)

    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    arr = []
    for tweet in tweets:
        # print(dir(tweet))
        # print(tweet.geo)
        # ---
        tweet_text_blob = TextBlob(tweet.text)

        if tweet_text_blob.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet_text_blob.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        output_d = {"author": tweet.username, "timestamp": tweet.date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                    "status": tweet.text,
                    "polarity": round(tweet_text_blob.sentiment.polarity, 3),
                    "subjectivity": round(tweet_text_blob.sentiment.subjectivity, 3),
                    "sentiment": sentiment
                    }
        arr.append(output_d)
        # write_ndjson("test_file.json", output_d)
        # print(output_d)

        # print(tweet.text)
        # print(tweet.date)
        # print(type(tweet.date))
        # # print(f"formatted date {tweet.formatted_date}")
        # print(f"retweets {tweet.retweets}")
        # print(tweet.username)
        # print(tweet.favorites)
        # print(tweet.permalink)

    # sorted_v = sorted(arr, key=lambda k: k["timestamp"])
    sorted_v = sorted(arr, key=lambda k: datetime.strptime(
        k["timestamp"], "%Y-%m-%dT%H:%M:%S.%f%z"))

    write_ndjson("test_file.json", sorted_v)
    # print(sorted_v)
    print(dir(tweets[0]))
    # --

    # print(*[tweet.text for tweet in tweets])

    # def get_old_tweets(search_criteria, start_date, end_date):
