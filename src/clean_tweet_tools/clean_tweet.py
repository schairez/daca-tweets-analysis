
import re


# def remove_url(txt: str) -> str:
#     url_pattern = re.compile(r'https?://\S+|www\.\S+')
#     no_url = url_pattern.sub(r'', txt)

#     return no_url


def clean_tweet(txt: str) -> str:
    url_pattern = '(https?://\S+|www\.\S+)'
    twitter_handle_pattern = '(@[\w]*)'
    all_patterns = re.compile('|'.join([url_pattern, twitter_handle_pattern]))
    return all_patterns.sub(r'', txt)


# remove twitter handles @
# remove urls
# remove
# if __name__ == "__main__":
#     test_str = """
#     President Trump’s ban on #immigrant workers moves Texas in the wrong direction, business leaders say https://texastribune.org/2020/06/25/texas-business-immigrant-workers-h1b-h2b-economy/ via
# @TexasTribune #H1B #H1Bvisa #TXLege"""

#     print(clean_tweet(test_str))
