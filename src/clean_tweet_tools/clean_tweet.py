
import re


def clean_tweet(txt: str) -> str:
    """
    fn removes twitter handles, urls, and numerics from text
    ex:
    >>> test_str = "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute 27,000 of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via @USATODAY https://www.usatoday.com/story/news/politics/2020/03/30/dreamers-wake-up-call-pandemic-puts-daca-recipients-front-lines/2935336001/"
    >>> clean_tweet(test_str)
    "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute , of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via  "
    """
    url_pattern = '(https?://\S+|www\.\S+)'
    twitter_handle_pattern = '(@[\w]*)'
    numeric_pattern = '[0-9]+'
    all_patterns = re.compile(
        '|'.join([url_pattern, twitter_handle_pattern, numeric_pattern]))
    tweet = all_patterns.sub(r'', txt)
    # replace 2+ dots
    tweet = re.sub(r'\.{2,}', ' ', tweet)
    # get rid of extra spacing and extraneous quotes
    tweet = tweet.strip(' "\'')
    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s+', ' ', tweet)

    # return all_patterns.sub(r'', txt)
    return tweet

# nOTES:
# hashtags often explain the subject matter of the tweet
