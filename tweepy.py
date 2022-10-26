
import tweepy

api_key = 'hCFHlRkGYskEkcblkdfO59m'
api_key_secret = 'vHxF18itA8agk3kb8dkwlbkwDog0iKx9smcLaXJaXR4tWpw'
access_token = '29901-PJtVx5Od4kbksl32kslKAGkJd6Q'
access_token_secret = '0SLm6SrbI6kslblJQKMpzCVDaw9i0df4kbKlbUUmbchH2yJa3quZcRP'


auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.mentions_timeline(count = 1)
for tweet in public_tweets:
    print (tweet.text)
