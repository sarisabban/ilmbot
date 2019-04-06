#!/usr/bin/python

import urllib.request
import urllib.parse
import datetime
import requests
import twython
import random
import time
import bs4
import sys
import re
import os

# Twitter credentials
key				= ''
secret			= ''
token			= ''
token_secret	= ''

# RSS links:
RSS1 = 'http://feeds.bbci.co.uk/arabic/scienceandtech/rss.xml'
RSS2 = 'http://arabic.cnn.com/rss/cnnarabic_scitech.rss'
RSS3 = 'http://rss.dw.de/rdf/rss-ar-sci'
RSS4 = ''
RSS5 = ''

# A list of RSS links
RSSlist = [	RSS1,
			RSS2,
			RSS3,
			RSS4,
			RSS5]

# Website links and their regular expressions
Website1 = ('http://www.scientificsaudi.com/main/articles',
			'http://www.scientificsaudi.com/ss/[0-9].*')
Website2 = ('https://syr-res.com',
			'https://syr-res.com/article/[0-9].*?.html')
Website3 = ('http://n-scientific.org',
			'http://n-scientific.org/[0-9].*#')
Website4 = ('https://oloom.news',
			'https://oloom\.news/%.*')
Website5 = ('http://www.bbc.com/arabic/scienceandtech',
			'/arabic/science-and-tech-[0-9].*')
Website6 = ('https://arabicedition.nature.com/',
			'')												####################
Website7 = ('https://ara.reuters.com/news/internet',
			'/article/')

# A list websites and their regular expressions
Weblist = [	#Website1,
			Website2,
			#Website3,
			#Website4,
			#Website5,
			#Website6,
			Website7]

def Article(THEWEB):
	''' Get title and URL from a webpage '''
	web = urllib.request.urlopen(THEWEB[0])
	data = bs4.BeautifulSoup(web, 'lxml')
	URLs = set()
	for link in data.find_all('a'):
		ArL = link.get('href')
		if re.search(THEWEB[1], str(ArL)):
			URLs.add(urllib.parse.urljoin(THEWEB[0], ArL))
	URL = URLs.pop()
	article = urllib.request.urlopen(URL)
	articledata = bs4.BeautifulSoup(article, 'lxml')
	Title = articledata.title.text
	if re.search('–', Title):
		Title = Title.replace('–', '-')
	if re.search('Ř', Title):
		raise Exception('[-] Incorrect title encoding')
	else:
		return(Title, URL)

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
#	api = twython.Twython(key, secret, token, token_secret)
#	api.update_status(TheTweet)

def main():
	''' Run the script with a loop to by pass errors '''
	for attempts in range(10):
		dateSTR = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')
		try:
			choice = random.choice(['article', 'rss'])
			if choice == 'article':
				info = Article(random.choice(Weblist))
			elif choice == 'rss':
				info = RSS(random.choice(RSSlist))
			Tweet(info)
			print('\x1b[32m[+] Tweeted - {}\x1b[0m'.format(dateSTR))
			break
		except Exception as TheError:
			print('\x1b[31m[-] ERROR - {} {}\x1b[0m'.format(TheError, dateSTR))
			continue

if __name__ == '__main__': main()
