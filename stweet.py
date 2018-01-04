#tweet track

import re

def split_string(search_term):
	""" 
	Splits the search string to words with | in between
	It takes string as input and returns a sigle word
	Args:
        param1 (str): String from search term.

    Returns:
    	concatinated words with '|' after every word.
	"""
	
	try:
		words = search_term.split()
		s = ""
		for i, item in enumerate(words):
			if i == len(words)-1:
				s = s + item
			else:
				s = s + item + '|'
		return(s)

	except ValueError:
		return search_term



def tweet(search_term):
	"""
	Takes the parameter from split_string and searches for the words in tweets file.
	Args:
		param1 (str): Words to search in txt file.
	Returns:
		List of tweets containing the words from search term.
	"""

	tweet_bucket = []
	search_these= split_string(search_term)
	search_for = re.compile(search_these, re.IGNORECASE)
	try:
		with open ('ass_text.txt', 'rt') as tweet_file:
			for tweet_num, tweet in enumerate(tweet_file):
				if search_for.search(tweet) != None:
					tweet_lines = tweet.rstrip('\n')
					tweet_lines = tweet_lines.split("\t")
					tweet_bucket.append((tweet_num, tweet_lines))
		return(tweet_bucket)
		
	except FileNotFoundError:
		return("Tweet file not found.")

