import actions
import twitter_oauth

import time



# Part 1: Generate your OAUTH tokens
# This needs to be done after you've created the .creds file with CONSUMER_KEY and CONSUMER_SECRET
# open a terminal within vscode and run: 'source .creds'
#
# uncomment this line below when you want to get your OAUTH credentials. Follow the link it shows you, authorize the app, and enter the pin.
# Then enter the output into your .creds file just like the CONSUMER_KEY, but this time it will look like:
# OAUTH_TOKEN = <your_oauth_token>
# OAUTH_SECRET = <your_oauth_secret>

twitter_oauth.getOauthFull()

# comment this^ again after you've generated your OAUTH tokens




# before calling this, make sure you've run the command: 'source .creds' at least once in your terminal with the new OAUTH tokens. 
# this needs to happen every time you open or close the terminal to run the code.

#oauth = twitter_oauth.getOauthShort()

# need to get the user ID for your own account in order to 'like' a tweet
# alex, change this to the username for your tester acccount

#myId = actions.getUserIds(oauth, "zartestapi")[0]




#usernames = ["BAYC2745", "zachareid", "zartestapi"]
#actions.likeMostRecentTweetsFromUsernames(oauth, usernames, myId)


# when you want to run it all the time, you can use this:
# every 15 minutes and 15 seconds, I want to call the "likeMostRecentTweetsFromUsernames" function
#while True:
    #actions.likeMostRecentTweetsFromUsernames(oauth, usernames, myId)
    #time.sleep(915)

