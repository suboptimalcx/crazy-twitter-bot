import tweepy
from dotenv import load_dotenv
import os
import random
import time

load_dotenv()

#----------------------------------------------------------------#
def retweet_tweet_with_text(client, includedtext, maxresults):
    response = client.search_recent_tweets(
        query=f"{includedtext} lang:en -is:retweet", #i included tweets in english and excluded retweets, if you just want the text delete lines after {}
        max_results=maxresults,
        user_auth=True 
    )

    if response.data:
        for tweet in response.data:
            try:
                client.retweet(tweet.id)
                print(f"retweeted: {tweet.id}")
            except tweepy.TweepyException as e:
                print(f"failed to retweet: {tweet.id}: {e}")
    else:
        print("no tweets found :((")
#----------------------------------------------------------------#
#MADE FOR LEARNING PURPOSES DO NOT USE THIS FUNCTION! its against TOS lol

def reply_to_tweets(client, includedtext, replytext, maxresults): 
    client.get_users_followers(id=client.data.id) 
    response = client.search_recent_tweets(
        query=f"{includedtext} lang:en -is:retweet",
        max_results=maxresults,
        user_auth=True
    )
    if response.data:
            for tweet in response.data:
                try:
                    client.create_tweet(
                        text=replytext,
                        in_reply_to_tweet_id=tweet.id,
                        user_auth=True
                    )
                    print(f"replied to: {tweet.id}")
                except tweepy.TweepyException as e:
                    print(f"failed to reply to: {tweet.id}: {e}")
    else:
        print("no tweets found :((")
#----------------------------------------------------------------#
def post_random_tweet_from_file(client, txtfilename):
    tweet_text = []
    with open(f'./{txtfilename}') as file:
        tweet_text = [line.strip() for line in file if line.strip()]
    
    idx = random.randint(0, len(tweet_text)-1)
    try:
        client.create_tweet(
            text=tweet_text[idx],
            user_auth=True
            )
        print(f"posted a tweet!")
    except tweepy.TweepyException as e:
        print(f"failed to post tweet: {e}")
#----------------------------------------------------------------#            
def main():
    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET") 
    )

    #the free version runs out of requests very quickly 
    try:
        retweet_tweet_with_text(client, "#crrrrrrrazy",20)
    except tweepy.TooManyRequests as e:
        print("hit search rate limit waiting 15 minutes.....................")
        time.sleep(15 * 60)
        retweet_tweet_with_text(client, "#crazy",10)

    post_random_tweet_from_file(client, "./brillianttweetideas.txt")
        
#----------------------------------------------------------------#       

if __name__ == "__main__":
    main()