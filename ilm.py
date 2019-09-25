#!/usr/bin/python3

import re
import os
import bs4
import sys
import time
import random
import twython
import requests
import datetime
import urllib.parse
import urllib.request

# Twitter credentials
key          = ''
secret       = ''
token        = ''
token_secret = ''

# RSS links:
RSS1 = 'http://feeds.bbci.co.uk/arabic/scienceandtech/rss.xml'
RSS2 = 'http://arabic.cnn.com/rss/cnnarabic_scitech.rss'
RSS3 = 'http://rss.dw.de/rdf/rss-ar-sci'
RSS4 = 'http://feeds.reuters.com/reuters/scienceNews'#English
RSS5 = 'http://feeds.nature.com/nature/rss/current'#English
RSS6 = 'https://science.sciencemag.org/rss/twis.xml'#English

# A list of RSS links
RSSlist = [RSS1, RSS2, RSS3, RSS4, RSS5, RSS6]

def RSS(RSSURL):
	''' Get title and URL from an RSS link '''
	data = bs4.BeautifulSoup(requests.get(RSSURL).content, features='xml')
	items = data.findAll('item')
	item = items[random.randint(0, 9)]
	title = item.title.text
	link = item.link.text
	return(title, link)

def Tweet(TEXT):
	''' Tweet '''
	TheTweet = '{}\n{}\n#علوم'.format(TEXT[0], TEXT[1])
	api = twython.Twython(key, secret, token, token_secret)
	api.update_status(TheTweet)

def main():
	''' Run the script with a loop to by pass errors '''
	for attempts in range(10):
		dateSTR = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')
		try:
			info = RSS(random.choice(RSSlist))
			Tweet(info)
			print('\x1b[32m[+] Tweeted - {}\x1b[0m'.format(dateSTR))
			break
		except Exception as TheError:
			print('\x1b[31m[-] ERROR - {} {}\x1b[0m'.format(TheError, dateSTR))
			continue

if __name__ == '__main__': main()
