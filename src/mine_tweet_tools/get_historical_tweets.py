
import GetOldTweets3 as got
from typing import List


def get_tweets(query: str, start_date: str, end_date: str, top_only=True, max_tweets=1000) -> List:
    """
    start_date ex: 2020-06-01
    end_date ex: 2020-06-15
    """
    tweetCriteria = got.manager.TweetCriteria()\
                               .setQuerySearch(query)\
                               .setTopTweets(top_only)\
                               .setLang("en")\
                               .setSince(start_date)\
                               .setUntil(end_date)\
                               .setMaxTweets(max_tweets)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    return tweets
