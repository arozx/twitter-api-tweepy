import tweepy
import time
import webbrowser

#acess keys
consumer_key = "<enter key>"
consumer_secret = "<enter key>"

callback_uri = 'oob'
#Oauth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
redirect_url = auth.get_authorization_url()

webbrowser.open(redirect_url)
user_pin_input = input("Whats the pin value?")

print(user_pin_input)

auth.get_access_token(user_pin_input)
print(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)
