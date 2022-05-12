import actions
import twitter_oauth

import time
import json
import os

oauth = twitter_oauth.getOauthShort()

#actions.createTweet("Hello, world!", oauth)
#actions.likeATweet(oauth, "1524540450123644928")

user_of_interest = "BAYC2745"

actions.getUserId(oauth, user_of_interest)


# get time in MM/DD/YYYY format
#time_str = time.strftime("%m/%d/%Y")












users = actions.getLikingUsers(oauth, "1524494034122641408")
usernames = [u["username"] for u in users["data"]]
print(usernames)



# using oauth, structure this into a request
#curl --request POST 
#--url https://api.twitter.com/1.1/direct_messages/events/new.json 
#--header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
#--header 'content-type: application/json' 
#--data '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'
#twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'

request_url = "https://api.twitter.com/1.1/direct_messages/events/new.json"


access_token = os.environ.get("OAUTH_TOKEN")
access_token_secret = os.environ.get("OAUTH_SECRET")

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
import tweepy

# Authenticate access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API handler
api = tweepy.API(auth)
recipient_id = "360985120"  # ID of the user
api.send_direct_message(recipient_id, "Hoi hoi")