from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyser = SentimentIntensityAnalyzer()


def sentiment_analyzer_scores(sentence):
    sentiment_dict = analyser.polarity_scores(sentence)
    # print("{:-<40} {}".format(sentence, str(sentiment_dict)))

    if sentiment_dict['compound'] >= 0.05:
        return "positive"

    elif sentiment_dict['compound'] <= - 0.05:
        return "negative"

    else:
        return "neutral"
