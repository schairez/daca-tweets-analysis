
import re


def clean_tweet(txt: str) -> str:
    """
    fn removes twitter handles and urls from text
    """
    url_pattern = '(https?://\S+|www\.\S+)'
    twitter_handle_pattern = '(@[\w]*)'
    all_patterns = re.compile('|'.join([url_pattern, twitter_handle_pattern]))
    return all_patterns.sub(r'', txt)
