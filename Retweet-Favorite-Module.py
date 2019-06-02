# Purpose of code is to access Twitter APIs to retweet 
# and favorite tweets about Ariana Grande
import tweepy
import time
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print('Initializing ' + user.name + '.')

ari = {'songs': ['Yuh!', 'Baby I', 'I love The Way you make me feel', "You'll Never Know, honey", 
'Catch me at Honeymoon Avenue', "You know I'll always be Right There", '*whistle tones*',
'thank u, next', "i'll get your name written on my tattoed heart", 'lovin it, b', 
'u gotta gotta got to love me harder', 'i got one less problem', "break up with your girlfriend, i'm bored"
'i can be needy, way too damn needy', 'MOONLIGHT', "i'll break your heart right back", 
"i'll have a grande cloud pls", "new Piano, who dis', 'i stay daydreamin'", 'maybe you could be my baby',
'keep your hands on me..', "got me feelin' like a dangerous woman", "walkin' side to side", 
"you know i'm GREEDY", "EVERYDAY EVERYDAY EVERYDAY", "don't leave me lonely"],
}
api.update_status(random.choice(ari['songs']))

search = "Ariana Grande"
for tweet in tweepy.Cursor(api.search, search).items(25):
    try:
        tweet.retweet()
        print('I retweet Ari')
    except tweepy.TweepError as ari_not_available:
        print(ari_not_available.reason)
    except StopIteration:
        break 
search = "Ariana Grande"
for tweet in tweepy.Cursor(api.search, search).items(100):
    try:
        tweet.favorite()
        print('I favorite Ari')
    except tweepy.TweepError as ari_not_available:
        print(ari_not_available.reason)
    except StopIteration:
        break
