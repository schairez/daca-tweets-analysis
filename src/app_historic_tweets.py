from mine_tweet_tools.get_historical_tweets import get_tweets
from clean_tweet_tools.clean_tweet import clean_tweet
from nltk_tweet_tools.sentiment_scores import sentiment_analyzer_scores as get_sent_scores
from file_tools.json_tools import write_JSON_file
from datetime import datetime, timedelta
from date_tools.tools import get_date_ranges_gen
from typing import List, Dict
import logging
import time
import calendar

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)d %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging


def prep_tweet_data(arr_tweet_objs: List) -> List[Dict[str, str]]:
    arr = []
    for tweet in arr_tweet_objs:
        dt = tweet.date
        tweet_clean = clean_tweet(tweet.text)
        output_dict = {
            "author": tweet.username,
            "timestamp": dt.strftime("%Y-%m-%dT%H:%M:%S") + str(dt.microsecond) + 'Z',
            "status": tweet.text,
            "sentiment": get_sent_scores(tweet_clean)
        }
        arr.append(output_dict)
    return sorted(arr, key=lambda k: k["timestamp"])


def main():
    date_ranges_list = list(get_date_ranges_gen('2020-06-17', '2020-06-28'))
    for date_tuple in date_ranges_list:
        month_idx = int(date_tuple[0][5:7])
        print(month_idx)
        month_abbr_text = calendar.month_abbr[month_idx]
        tweet_data = get_tweets("DACA", *date_tuple)
        log.info(
            f"Got list of tweed data for date:{date_tuple[0]} with len: {len(tweet_data)}")
        tweet_data_clean = prep_tweet_data(tweet_data)
        log.info(f"tweet data objects are preprocessed")
        # write_JSON_file(
        #     f'../data/data_json_lines/{date_tuple[0]}.jsonl', tweet_data_clean, json_lines=True)
        write_JSON_file(
            f'../data/data_json_lines/{month_abbr_text}.jsonl', tweet_data_clean, json_lines=True)
        time.sleep(2)


if __name__ == "__main__":
    main()
    # print(list(get_date_ranges_gen('2020-01-01', '2020-05-01')))
