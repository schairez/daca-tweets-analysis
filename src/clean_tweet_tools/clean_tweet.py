
import re


def clean_tweet(txt: str) -> str:
    """
    fn removes twitter handles, urls, and numbers from text
    ex:
    >>> test_str = "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute 27,000 of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via @USATODAY https://www.usatoday.com/story/news/politics/2020/03/30/dreamers-wake-up-call-pandemic-puts-daca-recipients-front-lines/2935336001/"
    >>> clean_tweet(test_str)
    "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute , of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via  "
    """
    url_pattern = '(https?://\S+|www\.\S+)'
    twitter_handle_pattern = '(@[\w]*)'
    number_pattern = '[0-9]+'
    all_patterns = re.compile(
        '|'.join([url_pattern, twitter_handle_pattern, number_pattern]))
    return all_patterns.sub(r'', txt)
