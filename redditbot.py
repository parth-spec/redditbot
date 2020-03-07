import praw
import config
import time
import os

def bot_login():
    print("Logging In....")
    re=praw.Reddit(client_id=config.client_id,
                client_secret=config.client_secret,
                username= config.username,
                password=config.password,
                user_agent='liberalbot by /u/narendermodizindaba')
    print("Logged In....")
    return re
def run_bot(re,comments_replied_to):
    print("obtaining 5000 comments....")
     
    for comment in re.subreddit('FuckYouKaren').comments(limit=5000):
        if "karen" in comment.body and comment.id not in comments_replied_to and comment.author != re.user.me():
            print("string with \"karen\" found in comments"+comment.id)
            comment.reply("Dont make fun of me or my precious child.Stop making fun of us or you will be contected by my lawyer ")
            print("Replied to comment"+ comment.id)
            comments_replied_to.append(comment.id)
            with open ("comments_replied_to.txt","a") as f:
                f.write(comment.id + "\n")
                print("Sleeping for 10 seconds zzzz")
                #sleep for 600 seconds
                time.sleep(600)
             

   
    
def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to=[]
    else:
        with open("comments_replied_to.txt","r") as f:
            comments_replied_to=f.read()
            comments_replied_to=comments_replied_to.split("\n")
            comments_replied_to=list(filter(None,comments_replied_to))
    return comments_replied_to

re=bot_login()
comments_replied_to=get_saved_comments()
while True:
    run_bot(re,comments_replied_to)


 

