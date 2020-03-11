import tweepy

from tweepy.auth import OAuthHandler

print("Hello world")


CONSUMER_KEY = "pZsFxQc02cs1WEjJZUKaLyk18"
COSUMER_SECRET = "lPS8WoyFJCGDOL6LdEwnM0chBq2pmkVaYSPr8xVWeRWVM9B9Yk"
ACCESS_KEY = "1145666867480186885-FGCzNoiOQDPusYfblMvWdTrLgXwRaN"
ACCESS_SECRETE = "3quHzqTT2fJ6fY597GjbWT1RualgifolIdFhjYLYdnN1x"


auth = tweepy.OAuthHandler(CONSUMER_KEY, COSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRETE)
api = tweepy.API(auth)
