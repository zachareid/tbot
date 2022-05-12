import os
import json
import requests
import time
# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'


def getUserIds(oauth, user_names):
    fields = "created_at,description"
    name_param = user_names
    # check if its a list
    if isinstance(user_names, list):
        # make this a comma-separated string
        name_param = ",".join(user_names)
    params = {"usernames": name_param, "user.fields": fields}
    response = oauth.get(
    "https://api.twitter.com/2/users/by", params=params)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print(response.json())
    # get the id
    output = [user["id"] for user in response.json()["data"]]
    return output


def getRecentTweetsFromUsers(oauth, user_ids):
    max_res = 50
    search_url = "https://api.twitter.com/2/tweets/search/recent?max_results={}".format(max_res)
    query_params = {'query': '(to:' + ' OR to:'.join(user_ids) + ') is:reply', 'tweet.fields': 'author_id,id,created_at'}
    json_response = connect_to_endpoint(search_url, query_params)
    return json_response

# #nowplaying (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible) (place_country:US OR place_country:MX OR place_country:CA) -horrible -worst -sucks -bad -disappointing
def getPositiveTweetsWithKeyword(oauth, keyword):
    max_res = 50
    sentiment_string = " (happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely OR incredible OR unreal) -horrible -worst -sucks -bad -disappointing"
    search_url = "https://api.twitter.com/2/tweets/search/recent?max_results={}".format(max_res)
    query_params = {'query': keyword + sentiment_string, 'tweet.fields': 'author_id,id,created_at'}
    json_response = connect_to_endpoint(search_url, query_params)
    return json_response

def getTweetsWithKeywordOrHashtag(oauth, keyword):
    max_res = 50
    search_url = "https://api.twitter.com/2/tweets/search/recent?max_results={}".format(max_res)
    query_params = {'query': keyword, 'tweet.fields': 'author_id,id,created_at'}
    json_response = connect_to_endpoint(search_url, query_params)
    return json_response

def getRecentTweetIdsFromUsers(oauth, user_ids):
    resp = getRecentTweetsFromUsers(oauth, user_ids)
    ids = []
    for tweet in resp['data']:
        ids.append(tweet['id'])
    return ids

def likeATweet(oauth, tweet_id, myId):
    payload = {"tweet_id": tweet_id}
    # Making the request
    response = oauth.post("https://api.twitter.com/2/users/{}/likes".format(myId), json=payload)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

def likeMostRecentTweetsFromUsernames(oauth, user_names, myId):
    print("=========================================================")
    print("            Running likeMostRecentTweetsFromUsernames")
    print("            -- for usernames: {}".format(user_names))
    print("            Time: {}".format(time.ctime()))
    print("=========================================================")
    user_ids = getUserIds(oauth, user_names)
    tweets = getRecentTweetsFromUsers(oauth, user_ids)
    count = 0
    for tweet in tweets['data']:
        print("=========================================================")
        print("Tweet " + str(count) + " of " + str(len(tweets['data'])))
        printTweet(tweet)
        #likeATweet(oauth, tweet['id'], myId)
        count += 1

def printTweet(tweet):
    tweet_id = tweet['id']
    author_id = tweet['author_id']
    text = tweet['text']
    created_at = tweet['created_at']
    print("Tweet ID: {}".format(tweet_id))
    print("Author ID: {}".format(author_id))
    print("Text: {}".format(text))
    print("Created at: {}".format(created_at))




# other ones to reference but not using
def getTweets(oauth):
    params = {"ids": "1278747501642657792", "tweet.fields": "created_at"}
    response = oauth.get("https://api.twitter.com/2/tweets", params=params)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

def createTweet(text, oauth):
    payload = {"text": text}
    response = oauth.post("https://api.twitter.com/2/tweets",json=payload)
    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    return json_response

def getLikingUsers(oauth, tweet_id):
    response = oauth.get(
    "https://api.twitter.com/2/tweets/{}/liking_users".format(tweet_id))
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    return json_response



# these are helpers
def bearer_oauth(r):
    bearer_token = os.environ.get("BEARER_TOKEN")
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
# end helpers

