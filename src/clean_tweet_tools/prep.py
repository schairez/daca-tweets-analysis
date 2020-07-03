
import re
# from nltk import word_tokenize
from nltk.tokenize.casual import TweetTokenizer
import string


# NOTE:
# , prep_for_model="sent" version?; we'll see as I add more preprocessing models, I may have to
# alter the arg defn.


class PreprocessText(object):
    def __init__(self, for_sent=True, for_ngram=False):
        if for_sent == for_ngram:
            raise ValueError(
                "for_sent and for_ngram cannot both be True or both be False. Pick one or the other.")
        self._for_sent = for_sent
        self._for_ngram = for_ngram

    def prep(self, text: str) -> str:
        return _prep_tweet_for_sent(text) if self._for_sent \
            else _prep_tweet_for_ngram(text)

        # NOTE:
        # hashtags often explain the subject matter of the tweet
        # since with VADER, punctuations such as "!" increases the magnitude
        # of intensity of the score, we don't remove punctuation marks for
        # sent scores, but for an N-gram model it's useful to get rid of non-word
        # characters
        # TweetTokenizer focuses on hashtags too, keeps the hashtag in place

        # TODO:
        # [x]get rid of ellipsis "..."
        # [x]get rid of commas, periods, slashes, paranthesis,and other special chars
        # []&amp; in tweets ?
        # for tokenization
        # [x]need to strip out links
        # [x]need to strip out special characters barring @ and # sign

# both:
# remove urls
# remove numerics

# dont need twitter handles for sentiment analysis
# only need "!" to mark inflection for sentiment analysis; we can leave "#" and "?" alone for now


def _prep_tweet_for_sent(text: str) -> str:
    """
    fn removes twitter handles, urls,numerics, and whitespace from text
    ex:
    >>> test_str = "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute 27,000 of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via @USATODAY https://www.usatoday.com/story/news/politics/2020/03/30/dreamers-wake-up-call-pandemic-puts-daca-recipients-front-lines/2935336001/"
    >>> prep_tweet_for_sent(test_str)
    "DREAMers' wake-up call: Pandemic puts DACA recipients on front lines“ They constitute , of the doctors, nurses, paramedics and other health care workers on the front lines fighting the #coronavirus pandemic. Via"
    """

    tweet = _common_text_preprocessing(text)
    tweet = _remove_handles_from_text(tweet)
    tweet = _remove_punctuation_chars_from_text(
        tweet, exclude_end_of_line_chars=True)

    return tweet


def _prep_tweet_for_ngram(text: str) -> list:
    """
    tokenizes a sentence into words. Utilizes TweetTokenizer which
    respects hashtags, commonly used to derive context in twitter statuses 
    """

    text = _common_text_preprocessing(text)
    text = _remove_punctuation_chars_from_text(
        text, exclude_end_of_line_chars=False)

    # reduce_len to collapse repeated characters
    # preserve_case=False to lowercase the text prior to tokenization
    tknzr = TweetTokenizer(preserve_case=False, reduce_len=True)
    tokens = tknzr.tokenize(text)
    return tokens


def _common_text_preprocessing(text: str) -> str:
    text = _remove_urls_from_text(text)
    text = _remove_numeric_from_text(text)
    text = _remove_quotes_from_text(text)
    text = _remove_ellipsis_from_text(text)
    text = _remove_extra_spaces_from_text(text)
    return text


def _remove_urls_from_text(text: str) -> str:
    return re.sub(r'(www|https?)\S+', '', text)


def _remove_numeric_from_text(text: str) -> str:
    return re.sub(r'\d+', '', text)


def _remove_quotes_from_text(text: str) -> str:
    return text.replace('"', '')


def _remove_ellipsis_from_text(text: str) -> str:
    return re.sub(r'\.{2,}', ' ', text)


def _remove_handles_from_text(text: str) -> str:
    """
    removes userhandles. ex: @JohnDoe 
    """
    return re.sub(r'(@[\w]*)', '', text)


def _remove_extra_spaces_from_text(text: str) -> str:
    """
    Replace multiple spaces with a single space
    """
    return re.sub(r'\s+', ' ', text)


def _remove_punctuation_chars_from_text(text: str, exclude_end_of_line_chars: bool = True) -> str:
    """
    exclude_end_of_line_chars such as ?!#\.
    """
    chars_to_remove = string.punctuation
    if exclude_end_of_line_chars:
        chars_to_remove = re.sub(r'[?!#\.]', '', chars_to_remove)

    return text.translate(str.maketrans('', '', chars_to_remove))
