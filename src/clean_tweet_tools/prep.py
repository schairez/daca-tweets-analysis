
import re
# from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer


def prep_tweet_for_sent(text: str) -> str:
    """
    fn removes twitter handles, urls, and numerics from text
    ex:
    >>> test_str = "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute 27,000 of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via @USATODAY https://www.usatoday.com/story/news/politics/2020/03/30/dreamers-wake-up-call-pandemic-puts-daca-recipients-front-lines/2935336001/"
    >>> prep_tweet_for_sent(test_str)
    "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute , of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via"
    """
    url_pattern = '(https?://\S+|www\.\S+)'
    twitter_handle_pattern = '(@[\w]*)'
    numeric_pattern = '[0-9]+'
    all_patterns = re.compile(
        '|'.join([url_pattern, twitter_handle_pattern, numeric_pattern]))
    tweet = all_patterns.sub(r'', text)
    # replace 2+ dots
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # get rid of extra spacing and extraneous quotes
    tweet = tweet.strip(' "\'')
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)

    return tweet

# NOTE:
# hashtags often explain the subject matter of the tweet
# since with VADER, punctuations such as "!" increases the magnitude
# of intensity of the score, we don't remove punctuation marks for
# sent scores, but for an N-gram model it's useful to get rid of non-word
# characters
# TweetTokenizer focuses on hashtags too, keeps the hashtag in place


def prep_tweet_for_ngram(text: str) -> list:
    # lower case tweet to normalize str
    tweet = text.lower()
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(tweet)
    return tokens

    # remove non-word chars
    # tweet = re.sub("\W", " ", tweet)
    # tokens = tweet.split()

# TODO:
# get rid of ellipsis "..."
# get rid of commas, periods, slashes, paranthesis,and other special chars
#
