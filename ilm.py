#!/usr/bin/python3
	  # <--- install module with pip3
import tweepy , urllib.request , re , random , datetime , time

#List of Websites:
Website1 = 'http://www.scientificsaudi.com/main/articles'
Website2 = 'https://syr-res.com'
Website3 = 'http://n-scientific.org'

#Regular Expression of Each Website:
WebRE1 = 'href="(http://www.scientificsaudi.com/ss/[0-9]*?)">'
WebRE2 = 'href="(https://syr-res.com/article/[0-9].*?.html)'
WebRE3 = 'href="(http://n-scientific.org/[0-9].*?)"\s.*?</h3>'

#Lists of Websites and their Regular Expressions
WEBlist	= [Website1 , Website2 , Website3]
RElist	= [WebRE1 , WebRE2 , WebRE3]

#Schedualing:
TweetTime1 = '19:00'
TweetTime2 = '20:00'
SleepTime  = 61

#Twitter Credentials:
consumer_key		= ''
consumer_secret		= ''
access_token		= ''
access_token_secret	= ''

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
def GetLink (Website , RegularExpression):
	'''Parses a website, gets all links that satisfy the given regular expression with their titles, then returns a random tuple with link and the page's title'''
	web = urllib.request.urlopen(Website)
	URLs = list()
	for line in web:
		line = line.decode()
		article = re.findall(RegularExpression , line)
		if article == []:
			continue
		else:
			URLs.append(article[0])
	random.shuffle(URLs)
	URL=URLs[0]

	web = urllib.request.urlopen(URLs[0])
	for line in web:
		line = line.decode()
		article = re.findall('<title>(.*?)</title>' , line)
		if article == []:
			continue
		else:
			TITLE = article[0]
	return(URL , TITLE)



def Tweet (WebList , Relist):
	for TheWeb , TheRE in zip(WebList , Relist):
		try:
			Result = GetLink(TheWeb , TheRE)
			TheTweet = Result[1] + '\n' + Result[0] + '\n' + '#علوم'
			api.update_status(TheTweet)
			print('\x1b[34m' + '[+] Tweet at ' + dateSTR + '\x1b[0m' + '\n' + TheTweet + '\n')
			time.sleep(SleepTime)

		except Exception:
			print('\x1b[31m' + '[-] ERROR' + '\x1b[0m')
			time.sleep(SleepTime)
#-----------------------------------------------------------------------------------------------------------
while True:
	dateSTR = datetime.datetime.now().strftime('%H:%M')
	if dateSTR == TweetTime1:
		Tweet(WEBlist , RElist)
	time.sleep(2700)
	if dateSTR == TweetTime2:
		Tweet(WEBlist , RElist)
	time.sleep(79200)
