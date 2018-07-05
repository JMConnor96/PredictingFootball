import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time

# Insert Twitter key and secret into here
twitter_key = ''
twitter_secret = ''
twitter_token = ''
twitter_token_secret = ''

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
