from mine_tweet_tools.get_historical_tweets import get_tweets
from clean_tweet_tools.clean_tweet import clean_tweet
from nltk_tweet_tools.sentiment_scores import sentiment_analyzer_scores as get_sent_scores
from file_tools.json_tools import write_JSON_file
from datetime import datetime, timedelta
from date_tools.tools import get_date_ranges_list
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging


def main():
    # start_date = datetime(2020, 1, 1)
    # end_date = datetime.now()
    date_ranges_list = list(get_date_ranges_list('2020-01-01', '2020-05-01'))

    pass


if __name__ == "__main__":
    print(list(get_date_ranges_list('2020-01-01', '2020-05-01')))
