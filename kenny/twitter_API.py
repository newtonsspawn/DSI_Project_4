import psycopg2
import tweepy
import json

# Importing postgres credentials
from postgres_credentials import *

# Importing twitter credentials
from twitter_credentials import *


def autorize_twitter_api():
    """
    This function gets the consumer key, consumer secret key, access token
    and access token secret given by the app created in your Twitter account
    and authenticate them with Tweepy.
    """
    # Get access and costumer key and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth


def create_tweets_table(term_to_search):
    """
    This function open a connection with an already created database and
    creates a new table to store tweets related to a subject specified by the
    user.
    """

    # Connect to Twitter Database created in Postgres
    conn_twitter = psycopg2.connect(dbname=dbnametwitter, user=usertwitter,
                                    password=passwordtwitter, host=hosttwitter,
                                    port=porttwitter)

    # Create a cursor to perform database operations
    cursor_twitter = conn_twitter.cursor()

    # with the cursor now, create two tables, users twitter and the
    # corresponding table according to the selected topic
    cursor_twitter.execute(
        "CREATE TABLE IF NOT EXISTS twitter_users (user_id VARCHAR PRIMARY "
        "KEY, user_name VARCHAR);")

    query_create = "CREATE TABLE IF NOT EXISTS %s (id SERIAL, created_at " \
                   "timestamp, tweet text NOT NULL, user_id VARCHAR, " \
                   "retweetcount int, PRIMARY KEY(id), FOREIGN KEY(user_id) " \
                   "REFERENCES twitter_users(user_id));" % (
            "tweets_" + term_to_search)
    cursor_twitter.execute(query_create)

    # Commit changes
    conn_twitter.commit()

    # Close cursor and the connection
    cursor_twitter.close()
    conn_twitter.close()
    return
