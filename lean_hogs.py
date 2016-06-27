# data_site_1='https://www.quandl.com/api/v3/datasets/ODA/PPORK_USD'
import sys
import os

import quandl
from twython import Twython

def main():
    #quandl.get('CHRIS/CME_LN1')
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

def send_dummy_tweet(s):
    print(s)

def send_tweet(s,twitter):
    twitter.update_status(status=s)
    
if __name__=="__main__":
    main()

