from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Tuple

analyser = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(sentence: str) -> Tuple[str, float]:
    sentiment_dict = analyser.polarity_scores(sentence)

    compound_sent_score: float = sentiment_dict['compound']
    if compound_sent_score >= 0.05:
        return ("positive", compound_sent_score)

    elif compound_sent_score <= - 0.05:
        return ("negative", compound_sent_score)

    else:
        return ("neutral", compound_sent_score)


# TIME FORMAT
# 2020-06-19T00:12:45.511Z
