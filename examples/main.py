import tweepy
import time

# Authentication details. To obtain these, visit dev.twitter.com
consumer_key = 'your-consumer-key-here'
consumer_secret = 'your-consumer-secret-here'
access_key = 'your-access-key-here'
access_secret = 'your-access-secret-here'

# This is the list of usernames that the bot will try to claim
username_list = ['username1', 'username2', 'username3']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# This is the main loop of the bot
while True:
    # Check if each username is available
    for username in username_list:
        try:
            # Try to create a user with the specified username
            user = api.create_user(username)

            # If successful, print a message and break out of the loop
            print(f'Successfully claimed username: {username}')
            break
        except tweepy.TweepError:
            # If the username is not available, print a message and try the next one
            print(f'Username {username} is not available')

    # Sleep for 10 seconds before checking again
    time.sleep(10)