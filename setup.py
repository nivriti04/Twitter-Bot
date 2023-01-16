#helps import all features of tweepy
import tweepy
import time
api_key= "t8xGHbTgupAhpPftZ5M0xGdKp"
api_secret= "TKSGiW4L56y1XiwcYxUtaeX7L5aPWifF2yMocOSknKd0xGobWQ"
bearertoken = "AAAAAAAAAAAAAAAAAAAAAICKkwEAAAAAzAHBOrlb0h%2FM8BQdaUGDAO5DdLg%3DP9TSf4BrffSfWq5JGXZAC0ymDRuUyErEq20rT9CKRu6xFs3Hae"
access_token = "1608193907656982532-us66OrkkitULJMrAFhSwHrkr9cI5tZ"
access_token_secret = "U7b7qASTEm4lWLdY9IoT2D259RSmC3ZNEe81Ek4w8Ql66"

#accesses the Twitter API as a client instance of tweepy
client = tweepy.Client(bearertoken, api_key, api_secret, access_token,access_token_secret)

#for some older tweepy features
auth=tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api =  tweepy.API(auth)

#creates a tweet
#client.create_tweet(text="Hello Twitter")

#used to like a tweet
#client.like(1608534170971635712)

#used to retweet a tweet
#client.retweet(1608534170971635712)

#used to reply to a tweet
#client.create_tweet(in_reply_to_tweet_id=1608534170971635712, text="hello User")

#searches for each tweet in the home timeline and prints it
#tweet.text to display text and tweet.id to get the tweet id
#for tweet in api.home_timeline():
   # print(tweet.id)

# how to get twitter id of an account
#person=client.get_user(username="bot_project2022").data.id

#how to print this person's tweet in the console
#for tweet in client.get_users_tweets(person).data:
    #print(tweet.text)

#twitter stream- used to get tweets as they are posted on twitter


class MyStream (tweepy.StreamingClient):
    # comes when the stream is alive
    def on_tweet (self, tweet):
       #print ("Connected")
       
       #called when the stream detects a tweet matching the criteria
       
            #referenced tweets tells us whether a certain tweet is a retweet or a reply
            #if its property is set to none, it only gives us original tweets
           #if tweet.referenced_tweets == None:
                print (tweet.text)
                try:
                    client.retweet(tweet.id)
                except Exception as errpr:
                    print ("error")
                
                #time.sleep(0.2)
                
stream = MyStream(bearer_token=bearertoken)

rule = tweepy.StreamRule("(#waterloo OR #loo) (-is:retweet -is:reply)")

stream.add_rules(rule, dry_run="True")
stream.filter()

#searching for tweets having one of the above words;
#for term in search_terms:
  #  stream.add_rules(tweepy.StreamRule(term))
    
    #used to filter out only original tweets
 #   stream.filter(tweet_fields=["referenced_tweets"])
    
    
    #how to like a tweet
class MyStream(tweepy.StreamingClient):
        
  def on_tweet(self, tweet):
        try:
          print(tweet.text)
          client.like(tweet.id)
          
        except Exception as error:
            print(error)  
         
         
        time.sleep(0.2)   
stream= MyStream(bearer_token=bearertoken)

stream.add_rules(tweepy.StreamRule("#waterloo OR #loo"), dry_run=True)
stream.filter()
