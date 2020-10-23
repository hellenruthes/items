import tweepy as tw
import pandas as pd
from gcloud import storage
from google.cloud import bigquery

def hello_world(request):
 
    request_json = request.get_json()


    consumer_key = 'Add API KEY' 
    consumer_secret = 'Add API key secret'
    access_token = 'Add access token'
    access_token_secret = 'Add access_token_secret'


    #Autentication 
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
    public_tweets = api.home_timeline()



    #variables
    search_brand = 'boticário '
    search_boticario_line = "#eudora"
    exclude_retweets = ' -filter:retweets'
    query_tw= search_brand + exclude_retweets
    language = 'pt'
    sort_by= 'created_at -asc'
    tweets_number = 50


   #get twitter
    cursor_tweets = tw.Cursor(api.search,q=query_tw,lang=language,sort_by=sort_by).items(tweets_number) 
    
    tweets = [['',tweet.user.name, tweet.text, tweet.created_at] for tweet in cursor_tweets]
    tweet_csv = pd.DataFrame(data=tweets, columns=['id','twitter_user_name', "twitter_content","twitter_created_at"])
    tweet_csv.to_csv('/tmp/tweet.csv')

    df = pd.DataFrame(data=tweets).to_csv(sep=";", index=False, encoding="UTF-8")
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('boticario-hruthes-twitter-incoming')
    blob = bucket.blob('boticario-hruthes-twitter-incoming')
    blob.upload_from_filename('/tmp/tweet.csv', content_type='text/csv')

    return f'Searching for twitters...'
