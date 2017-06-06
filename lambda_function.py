#!/usr/bin/env python

import sys
import os

import random

import yaml
from twython import Twython

def lambda_handler(event,context):
    with open('.app_key','r') as f:
        APP_KEY=f.read()
    with open('.app_secret','r') as f:
        APP_SECRET=f.read()

    if (not APP_KEY) or (not APP_SECRET):
        sys.exit("Could not load app key or secret")
    else:
        print("App key: " + APP_KEY)
        print("App secret: " + APP_SECRET)

    with open('.usr_key') as f:
        OAUTH_TOKEN = f.read()
    with open('.usr_secret') as f:
        OAUTH_TOKEN_SECRET = f.read()

    if (not OAUTH_TOKEN) or (not OAUTH_TOKEN_SECRET):
        sys.exit("Could not load usr key or secret")
    else:
        print("User key: " + APP_KEY)
        print("User secret: " + APP_SECRET)

    twitter=Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

    #Form our tweet (very basic, will be more complex in the future)
    with open("tweet_list.yml",'r') as f:
        tweet_dict=yaml.load(f)
    
    tweet_subset=tweet_dict['generic']
    
    tweet=random.sample(tweet_subset,1)
    
    send_dummy_tweet(tweet[0])

    #if choice==-1:
    #    tweet_string=form_tweet_fun_fact()
    #elif choice==1:
    #    tweet_string=form_tweet_closing_price(data)
    #elif choice==2:
    #    print('Ummm wat');
    #    sys.exit()
    #else:
    #    sys.exit("Something went wrong")
        
    # Send the tweet
    #send_dummy_tweet(tweet_string)
    send_tweet(tweet[0],twitter)

def send_dummy_tweet(s):
    print(s)

def send_tweet(s,twitter):
    twitter.update_status(status=s)
