#!/usr/bin/python

import urllib.request
import urllib.parse
import datetime
import requests
import twython
import hashlib
import random
import time
import bs4
import sys
import re
import os

#Terminal text colours
Black 	= '\x1b[30m'
Red	= '\x1b[31m'
Green	= '\x1b[32m'
Yellow	= '\x1b[33m'
Blue	= '\x1b[34m'
Purple	= '\x1b[35m'
Cyan	= '\x1b[36m'
White	= '\x1b[37m'
Cancel	= '\x1b[0m'

#Twitter credentials
key		= ''
secret		= ''
token		= ''
token_secret	= ''

#Instagram credentials
OAuth		= ''
insta = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(OAuth)

#Connecting to twitter
api = twython.Twython(key, secret, token, token_secret)

def md5(words):
	'''hashes a string'''
	hash_md5 = hashlib.md5()
	hash_md5.update(words.encode())
	return(hash_md5.hexdigest())

def Article():
	'''
	Parses a website, gets all links that satisfy the given
	regular expression with their titles, then returns a random
	tuple with a URL link and the page's title
	'''
	#Tuples of websites and their regular expressions
	Website1 = ('http://www.scientificsaudi.com/main/articles', 'http://www.scientificsaudi.com/ss/[0-9].*')
	Website2 = ('https://syr-res.com', 'https://syr-res.com/article/[0-9].*?.html')
	Website3 = ('http://n-scientific.org', 'http://n-scientific.org/[0-9].*#')
	Website4 = ('https://oloom.news', 'https://oloom\.news/%.*')
	Website5 = ('http://www.bbc.com/arabic/scienceandtech', '/arabic/science-and-tech-[0-9].*')
	Website6 = ('https://ara.reuters.com/news/internet', '/article/')
	#Lists of tuples: websites and their regular expressions
	WEBlist = [	Website1, Website2, Website3,
			Website4, Website5, Website6	]
	#Random choice
	random.shuffle(WEBlist)
	TheWeb = WEBlist[0]
	#Get article info
	web = urllib.request.urlopen(TheWeb[0])
	data = bs4.BeautifulSoup(web, 'lxml')
	URLs = set()
	for link in data.find_all('a'):
		ArL = link.get('href')
		if re.search(TheWeb[1], str(ArL)):
			URLs.add(urllib.parse.urljoin(TheWeb[0], ArL))
	URL = URLs.pop()
	article = urllib.request.urlopen(URL)
	articledata = bs4.BeautifulSoup(article, 'lxml')
	Title = articledata.title.text
	if re.search('–', Title):
		Title = Title.replace('–', '-')
	if re.search('Ř', Title):
		raise Exception('incorrect title encoding')
	else:
		return(Title, URL)

def RSS():
	'''Generates an episode tweet from RSS links'''
	#SoundCloud RSS
	SCurl = 'http://www.mstdfr.com/feed/?podcast=ilm'
	SCrss = requests.get(SCurl)
	SCdata = bs4.BeautifulSoup(SCrss.content, features='xml')
	SCitems = SCdata.findAll('item')
	SCitem = SCitems[0]
	Numb = SCitem.title.text.split(':')[0]
	Title = SCitem.title.text.split(':')[1]
	SndCld = SCitem.link.text
	#YouTube RSS
	YTurl = 'https://www.youtube.com/feeds/videos.xml?channel_id=UC_iBvLK04bFOzu3nZtZKePA'
	YTrss = requests.get(YTurl)
	YTdata = bs4.BeautifulSoup(YTrss.content, features='xml')
	YTID = YTdata.findAll('yt:videoId')[0].text
	YouTub = 'https://www.youtube.com/watch?v={}'.format(YTID)
	Users = 'اذا تبغوا تسجلوا لنا خرجة الحلقة:\nilm.fm/out'
	#Instagram media
#	IGurl = 'https://web.stagram.com/rss/n/ilm_fm'
#	IGurl = 'https://www.instagram.com/ilm_fm/'
#	IG = urllib.request.urlopen(IGurl)
#	IGdata = bs4.BeautifulSoup(IG, 'lxml')
#	IGitems = SCdata.findAll('script')
#	Media = 'X'
#	print(IGitems)
	TEXT = 'حلقة {} {}\n\n#SoundCloud #iTunes\n{}\n\n#YouTube\n{}\n\n{}'.format(Numb, Title, SndCld, YouTub, Users)
	return(TEXT)

def Tweet(choice):
	'''Tweet'''
	if choice == 'article':
		text = Article()
		TheTweet = '{}\n{}\n#علوم'.format(text[0], text[1])
#		api.update_status(TheTweet)
		return(True)
	elif choice == 'rss':
		TheTweet = RSS()
		#Do not repeat tweets
		if os.path.exists('.check') == False:
			cf = open('.check', 'w')
			cf.write('None')
			cf.close()
		check1 = md5(TheTweet)
		cf = open('.check', 'r')
		for line in cf:
			check2 = line
		cf.close()
		if check1 != check2:
			cf = open('.check', 'w')
			cf.write(check1)
			cf.close()
#			api.update_status(TheTweet)
			return(True)
		else:
			return(False)

def main():
	'''Run the script with a loop to by pass errors'''
	for attempts in range(10):
		dateSTR = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')
		try:
			tweeted = Tweet(sys.argv[1])
			if tweeted == True:
				print('{}[+] Tweeted - {}{}'
				.format(Green, dateSTR, Cancel))
				break
			elif tweeted == False:
				print('{}[-] Repeated Tweet - {}{}'
				.format(Red, dateSTR, Cancel))
				break
		except Exception as TheError:
			print('{}[-]{}{}{}'
			.format(Red, str(TheError), dateSTR, Cancel))
			continue

#if __name__ == '__main__': main()


rss = requests.get(insta).content.decode()
#data = bs4.BeautifulSoup(rss)


print(rss)
