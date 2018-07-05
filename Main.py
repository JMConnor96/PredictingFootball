import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time

twitter_key = 'J8cChKHci7VVv1OlcRpAUIiJS'
twitter_secret = 'iae1PqOGHNHl0BHpeAKY0XjkJWPgQWn6jN0Ve1xYI1MpbV6l1D'
twitter_token = '937323236529983488-ZUBip2AtNIU5IpKsXj2twEi4maLLZxA'
twitter_token_secret = '1J2wwf0341G7SRAnIynJe87H1gabPEdpc6LxgaFcRFEKm'

auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
auth.set_access_token(twitter_token, twitter_token_secret)
api = tweepy.API(auth)

class listener(StreamListener):

    def on_data(self, data):
        try:
            if 'RT' not in data:
                tweet = data.split(',"text":"')[1].split(',"source')[0]
                print(tweet)
                saveTweet = '::'+tweet+'.'
                saveFile = open('Test.txt', 'a')
                saveFile.write(saveTweet)
                saveFile.write('\n')
                saveFile.close()
                return True
        except BaseException as e:
            print('Failed'), str(e)
            time.sleep(5)

    def on_error(self, status):
        print(status)


twitter_stream = Stream(auth, listener())
twitter_stream.filter(languages=["en"], track=["#MUFC"])
