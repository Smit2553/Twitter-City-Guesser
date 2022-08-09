import shutil
from bing_image_downloader import downloader
from city import *
import sqlite3
import os
import tweepy
from dotenv import load_dotenv
from traceback import print_exc

load_dotenv()


def posttweet():
    city = get_city()
    try:
        shutil.rmtree('./image')
    except FileNotFoundError:
        pass
    downloader.download(f'{city[0]}', limit=1, output_dir='image', verbose=True)
    for subdir, dirs, files in os.walk('./image'):
        for file in files:
            path = (os.path.join(subdir, file))
            print(path)
    consumer_key = os.environ.get('CONSUMERKEY')
    consumer_secret = os.environ.get('CONSUMERSECRET')
    access_token = os.environ.get('ACCESSTOKEN')
    access_token_secret = os.environ.get('ACCESSTOKENSECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweettext = "Can you guess which city this image is from?"
    image_path = f"{path}"

    # to attach the media file
    tweet = api.update_status_with_media(tweettext, image_path)
    con = sqlite3.connect('tweet.db')
    cur = con.cursor()
    try:
        cur.execute('''CREATE TABLE tweets (
                       tweetid text,
                       city text
                       )''')
        con.commit()
    except:
        pass
    cur.execute(f"""INSERT INTO tweets VALUES
                (
                "{tweet.id}",
                "{city[0]}")
                """)
    con.commit()
    con.close()


posttweet()
