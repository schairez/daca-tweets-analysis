import tweepy
import config
import logging
# import requests.packages.urllib3 as urllib3
# import boto3

from requests.packages import urllib3
# from datetime import datetime
import datetime
import pytz
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


ReadTimeoutError = urllib3.exceptions.ReadTimeoutError
logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)


class MyStreamListener(tweepy.StreamListener):

    # def __init__(self, kinesis_client):
    # 	self.kinesis_client = kinesis_client

    def on_connect(self):
        print('Stream starting...')

    # def on_data(self, data):
    #     print(data)
    #     return True

    def on_status(self, status):
        print('**************')
        # print(dir(status))

        # filtering out retweets
        if hasattr(status, 'retweeted_status'):
            # print(f'retweet!!! {status.retweeted_status}')
            return

        # if hasattr(status, 'extended_tweet'):
        #     print(status.extended_tweet["full_text"])
        # else:
        #     # tweet < 140 chars
        #     print(status.text)

        # classic or extended tweet
        tweet_text = status.extended_tweet["full_text"] if hasattr(
            status, 'extended_tweet') else status.text

        # TODO: LOOK INTO QUOTED TWEETS

        city_loc = status.place.full_name if status.place else status.user.location
        username = status.user.screen_name

        print(tweet_text)
        print(city_loc)
        print(f"created_at {status.created_at}")
        # print(f"status user {status.user}")
        print(f"status user location{status.user.location}")
        print(f"status user screen_name {status.user.screen_name}")
        if status.place:
            print(f"full name {status.place.full_name}")

        # print(f"coords: {status.coordinates}")
        # print(f"status geo {status.geo}")

        # tweet = status.full_text

        # try:
        #     tweet = status.extended_tweet["full_text"]
        # except AttributeError:
        #     tweet = status.text

        # if hasattr(status, 'extended-tweet'):
        #     tweet = status.extended_tweet["full_text"]
        # else:
        #     tweet = status.text

        # status.retweet_count
        # status.favorite_count #likes

        # ___________
        # if hasattr(status, 'retweeted_status'):
        #     try:
        #         tweet = status.retweeted_status.extended_tweet["full_text"]
        #     except:
        #         tweet = status.retweeted_status.text
        # else:
        #     try:
        #         tweet = status.extended_tweet["full_text"]
        #     except AttributeError:
        #         tweet = status.text

        # ______________

        # print(dir(status))

        # print(tweet)
        # tweet_blob =

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:  # enhance your calm - message about rate limiting
            # returning False in on_error disconnects the stream
            print("Rate Limit Exceeded ")
            # time.sleep(15 * 60)
            # return False
        return False

# status place Place(_api=<tweepy.api.API object at 0x10c517910>, id='f995a9bd45d4a867', url='https://api.twitter.com/1.1/geo/id/f995a9bd45d4a867.json', place_type='city', name='Memphis', full_name='Memphis, TN', country_code='US', country='United States', bounding_box=BoundingBox(_api=<tweepy.api.API object at 0x10c517910>, type='Polygon', coordinates=[[[-90.135782, 34.994192], [-90.135782, 35.272849], [-89.708276, 35.272849], [-89.708276, 34.994192]]]), attributes={})

# status place Place(_api= < tweepy.api.API object at 0x101423910 > , id='8e9665cec9370f0f', url='https://api.twitter.com/1.1/geo/id/8e9665cec9370f0f.json', place_type='city', name='Minneapolis', full_name='Minneapolis, MN', country_code='US', country='United States', bounding_box=BoundingBox(_api= < tweepy.api.API object at 0x101423910 > , type='Polygon', coordinates=[[[-93.329515, 44.889964], [-93.329515, 45.051257], [-93.194578, 45.051257], [-93.194578, 44.889964]]]), attributes={})


# 5kb per tweet
# hashtags, location, text
# consumer_token = config.consumer_token


def start_stream(stream, **kwargs):
    try:
        stream.filter(**kwargs)
    except ReadTimeoutError:
        stream.disconnect()
        logger.exception("ReadTimeoutError exception")
        start_stream(stream, **kwargs)
    except Exception:
        stream.disconnect()
        logger.exception("Fatal exception. Consult logs.")
        start_stream(stream, **kwargs)

# start_stream(myStream, track=['A'], async=True)


# USCIS
trump_l = ['#Trump', '@realDonaldTrump', 'MAGA']
daca_l = ['#DACA', '#HereToStay', '#IBelongHere',
          '#Dreamers', '#DreamAct', '#DACArecipients']
blm_l = []
san_leandro_l = ["sanleandro"]
# defund_l = ["#Defund"]


# extract: user_name,
if __name__ == "__main__":
    # kinesis_client = boto3.client('kinesis')

    myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(
        config.consumer_token, config.consumer_secret)

    auth.set_access_token(config.access_token,
                          config.access_token_secret)

    # ---------
    api = tweepy.API(auth, wait_on_rate_limit=True)
    daca_query = "#DACA OR #undocumented OR #HereToStay OR #endDACA OR #EndDacaNow OR #Dreamers" \
        " OR #DreamAct OR #DACArecipients OR Deferred Action for Childhood Arrivals" \
        " OR Deferred Action for Illegal Childhood Arrivals" \
        " -filter:retweets"
    for status in tweepy.Cursor(api.search, q=daca_query,
                                tweet_mode='extended',  count=100,
                                lang="en",  include_entities=True, since="2019-06-01").items(10000):
        # if hasattr(status, "retweeted_status"):
        #     continue
        print(dir(status))
        # print(type(status))
        # print(dir(status))
        print(status.full_text)
        city_loc = status.place.full_name if status.place else status.user.location
        username = status.user.screen_name

        print(city_loc)
        print(f"created_at {status.created_at}")
        print(type(status.created_at))
        utc_created_at = status.created_at.replace(
            tzinfo=datetime.timezone.utc)
        print(f"created at tz {utc_created_at}")
        print(type(utc_created_at))
        # 2020-06-18 14:11:36+00:00
        print(f"username {username}")
        print(f"user followers count {status.user.followers_count}")
        print(f"user statuses count {status.user.statuses_count}")
        print(f"retweet_count {status.retweet_count}")
        print(f"favorite_count {status.favorite_count}")

    # print(status)
    # print(tweet.text)
    # print(dir(tweet))
    # print(tweet.created_at, tweet.text)
    # -------------

    # ---

    # stream = tweepy.Stream(auth,  myStreamListener, tweet_mode="extended",
    #                        wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    # stream.filter(track=['#DACA', '#HereToStay',
    #                      '#IBelongHere', '#Dreamers', ], is_async=True, languages=["en"])

    # ---

    # api = tweepy.API(auth)
    # me = api.me()
    # print(me.screen_name)c

    # redirect_url = auth.get_authorization_url()
    # print(redirect_url)
    # user_pin = "4070527"
    # print(auth.get_access_token(user_pin))

    # myStreamListener = MyStreamListener()
    # myStream = tweepy.Stream(listener=myStreamListener())
    # myStream.filter(track=['python'])
