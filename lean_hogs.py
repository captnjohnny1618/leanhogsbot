#!/usr/bin/env python

import sys
import os
import time
from datetime import date,timedelta

import random

import quandl
from twython import Twython

def main():

    # Set up our dates:
    today=date.today()
    a_week_ago=today-timedelta(days=7)
    today_datestr=today.strftime("%Y-%m-%d")
    a_week_ago_datestr=a_week_ago.strftime("%Y-%m-%d")

    if today.weekday()==0 or today.weekday()==6:
        is_weekend=True
    else:
        is_weekend=False
    
    # Grab leanhogs dataset from Quandl
    data=[];
    try:
        data=quandl.get('CHRIS/CME_LN1',start_date=a_week_ago_datestr,end_date=today_datestr)
    except: # Can't access internet; wait 30 minutes and try again
        print("Couldn't reach Quandl, sleeping and trying again")
        data=[];
        time.sleep(30*60);

    print(data)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
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

    # Form our tweet (very basic, will be more complex in the future)
    if not is_weekend:
        choice=random.randint(1,1);
    else:
        choice=-1

    if choice==-1:
        tweet_string=form_tweet_fun_fact()
    elif choice==1:
        tweet_string=form_tweet_closing_price(data)
    elif choice==2:
        print('Ummm wat');
        sys.exit()
    else:
        sys.exit("Something went wrong")
        
    # Send the tweet
    #send_dummy_tweet(tweet_string)
    send_tweet(tweet_string,twitter)

def form_tweet_closing_price(data):
    arr=data.Settle.values
    yest_settle=arr[len(arr)-1];
    today_settle=arr[len(arr)-2];
    tweet_string="The lean hogs market (CME) closed at $%.2f, a %.2f%% change over the last day of trading." % (today_settle,(yest_settle-today_settle)/yest_settle*100)
    return tweet_string

def form_tweet_fun_fact():
    return "Did you know hog is another word for pig?"

def send_dummy_tweet(s):
    print(s)

def send_tweet(s,twitter):
    twitter.update_status(status=s)
    
if __name__=="__main__":
    main()

