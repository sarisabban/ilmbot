#!/usr/bin/python3
	  # 	 # <--- install module with pip3
import tweepy , bs4 , urllib.request , re , random , datetime , time
from Keys import *

#Tuples of Websites and their Regular Expressions:
Website1 = ('http://www.scientificsaudi.com/main/articles' , 'http://www.scientificsaudi.com/ss/[0-9].*')
Website2 = ('https://syr-res.com' , 'https://syr-res.com/article/[0-9].*?.html')
Website3 = ('http://n-scientific.org' , 'http://n-scientific.org/[0-9].*#')

#Lists of Tuples: Websites and their Regular Expressions
WEBlist	= [Website1 , Website2 , Website3]

#Twitter Credentials Are Found in the Keys File.

#Print Our Logo In The Terminal:
print('''\x1b[32m
██╗██╗     ███╗   ███╗    ███████╗███╗   ███╗
██║██║     ████╗ ████║    ██╔════╝████╗ ████║
██║██║     ██╔████╔██║    █████╗  ██╔████╔██║
██║██║     ██║╚██╔╝██║    ██╔══╝  ██║╚██╔╝██║
██║███████╗██║ ╚═╝ ██║    ██║     ██║ ╚═╝ ██║
╚═╝╚══════╝╚═╝     ╚═╝    ╚═╝     ╚═╝     ╚═╝
\x1b[0m''')

#Connecting To Twitter:
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth)
print('\x1b[33m' + '[+] Connected To Twitter' + '\x1b[0m')
print('\x1b[35m' + '------------------------------' + '\x1b[0m')
#-----------------------------------------------------------------------------------------------------------
def GetLink(TheWeb , TheRE):
	'''Parses a website, gets all links that satisfy the given regular expression with their titles, then returns a random tuple with link and the page's title'''
	while True:
		try:
			web = urllib.request.urlopen(TheWeb)
			data = bs4.BeautifulSoup(web , 'html5lib')

			URLs = set()
			for link in data.find_all('a'):
				ArticleLinks = link.get('href')
				if re.search(TheRE , str(ArticleLinks)):
					URLs.add(ArticleLinks) 

			URL=URLs.pop()

			article = urllib.request.urlopen(URL)
			articledata=bs4.BeautifulSoup(article , 'html5lib')
			Title = articledata.title.text
			if re.search('Ř' , Title):
				print('\x1b[31m' + '[-] Error')
				print('Problem with page title encoding' + '\x1b[0m')
				continue
			else:
				
				return(Title , URL)
				break

		except Exception as TheError:
			print('\x1b[31m' + '[-] ERROR in GetLink function')
			print(TheError)
			print('\x1b[0m')


def Tweet (TheWeb , TheRE):
	'''Tweets a weblink and its title'''
	try:
		dateSTR = datetime.datetime.now().strftime('%H:%M')
		Result = GetLink(TheWeb , TheRE)
		TheTweet = Result[0] + '\n' + Result[1] + '\n' + '#علوم'
		api.update_status(TheTweet)
		print('\x1b[34m' + '[+] Tweet at ' + dateSTR + '\x1b[0m' + '\n' + TheTweet + '\n')

	except Exception as TheError:
		print('\x1b[31m' + '[-] ERROR in Tweet function')
		print(TheError)
		print('\x1b[0m')
#-----------------------------------------------------------------------------------------------------------
random.shuffle(WEBlist)
TheWebsite = WEBlist[0]
Tweet(TheWebsite[0] , TheWebsite[1])
