#!/usr/bin/python3
import tweepy , bs4 , urllib.request, urllib.parse , re , random , datetime , time

#Tuples Of Websites And Their Regular Expressions
Website1 = ('http://www.scientificsaudi.com/main/articles' , 'http://www.scientificsaudi.com/ss/[0-9].*')
Website2 = ('https://syr-res.com' , 'https://syr-res.com/article/[0-9].*?.html')
Website3 = ('http://n-scientific.org' , 'http://n-scientific.org/[0-9].*#')
Website4 = ('https://oloom.news' , 'https://oloom\.news/%.*')
Website5 = ('http://www.bbc.com/arabic/scienceandtech' , '/arabic/science-and-tech-[0-9].*')
Website6 = ('http://www.reuters.com/news/science' , '/article/')

#Lists of Tuples: Websites And Their Regular Expressions
WEBlist	= [Website1 , Website2 , Website3 , Website4 , Website5 , Website6] 

#Twitter Credentials
from keys import *

#Terminal Text Colours
Black 	= '\x1b[30m'
Red	= '\x1b[31m'
Green	= '\x1b[32m'
Yellow	= '\x1b[33m'
Blue	= '\x1b[34m'
Purple	= '\x1b[35m'
Cyan	= '\x1b[36m'
White	= '\x1b[37m'
Cancel	= '\x1b[0m'

#Connecting To Twitter
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth)
#-----------------------------------------------------------------------------------------------------------
#Functions
def GetLink(TheWeb , TheRE):
	''' Parses a website, gets all links that satisfy the given regular expression with their titles, then returns a random tuple with a URL link and the page's title '''
	web = urllib.request.urlopen(TheWeb)
	data = bs4.BeautifulSoup(web , 'lxml')
	URLs = set()
	for link in data.find_all('a'):
		ArticleLinks = link.get('href')
		if re.search(TheRE , str(ArticleLinks)):
			URLs.add(urllib.parse.urljoin(TheWeb, ArticleLinks))
	URL = URLs.pop()
	article = urllib.request.urlopen(URL)
	articledata = bs4.BeautifulSoup(article , 'lxml')
	Title = articledata.title.text
	if re.search('–' , Title):
		Title = Title.replace('–' , '-')
	if re.search('Ř' , Title):
		raise Exception('incorrect title encoding')
	else:	
		return(Title , URL)

def Tweet (TheWeb , TheRE):
	''' Tweets a weblink and its title '''
	Result = GetLink(TheWeb , TheRE)
	TheTweet = Result[0] + '\n' + Result[1] + '\n' + '#علوم'
	api.update_status(TheTweet)
#-----------------------------------------------------------------------------------------------------------
for attempts in range(1000):
	random.shuffle(WEBlist)
	TheWebsite = WEBlist[0]
	dateSTR = datetime.datetime.now().strftime('%d %B %Y @ %H:%M')
	try:
		Tweet(TheWebsite[0] , TheWebsite[1])
		print(Green + '[+] Tweeted -' , dateSTR + Cancel , TheWebsite[0])
		break
	except Exception as TheError:
		print(Red + '[-]' , str(TheError) , dateSTR + Cancel , TheWebsite[0])
		continue
