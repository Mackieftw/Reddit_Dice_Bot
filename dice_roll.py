#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import Required Libraries

import praw
import pdb
import re
import os
import time
import datetime
import random
from bot_info import *

now = datetime.datetime.now() #sets datetime with system
current_hour = now.hour #takes hours from the now var  (Maybe change from 24 hour time)
current_min = now.minute #takes mins from the now var

#Set up User agent for session and login to Reddit
user_agent = ("DiceRoll v0.1")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)
t = 1

while t > 0:
	
	
#Checks if a file is created to save replied comment.id's to. 
# This will stop you from replying to the sae comment multiple times.
	if not os.path.isfile("diceroll_text.txt"):
	diceroll_text = []
#If the file already exists, opens and reads.	
	else:
		with open ("diceroll_text.txt", "r") as f:
			diceroll_text = f.read()
			diceroll_text = Replied_To.split("\n")
			diceroll_text = filter(None, diceroll_text)


#Now we setup the subreddit we want to check, I picked Politics.
#Following this, setup comment reading in said subreddit and a limiter.(This is to go with Reddit API rules)
	subreddit = r.get_subreddit("politics")
	comments = subreddit.get_comments(limit=100)
	#Get the diceroll before getting subreddit info
	dice_roll = random.sample(range(1,6), 1)
#Here we check through the comments of the Hottest 5 posts, 
#Check for crieteria (This case build a wall) and if met reply to it
	for comments in subreddit.get_hot(limit=5):
	
		if comment.id not in diceroll:
		
			if comment.body == "!diceroll" :
			
				comment.reply("You rolled a ", dice_roll)
			
				print ("Bot replied to", subreddit, submission.id, comment.id)
			
				diceroll_text.append(comment.id)
#Write the comment.id to a file to prevent us from commenting again
	with open ("diceroll_text.txt", "W") as f:
		for post_id in Replied_To:
			f.write(comment.id + "\n")
			time.sleep(900)
