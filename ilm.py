#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tweepy
import re
import urllib.request
import random
import datetime

# Tuples of Websites and their Regular Expressions:
Website1 = ('http://www.scientificsaudi.com/main/articles',
            'href="(http://www.scientificsaudi.com/ss/[0-9]*?)">')

Website2 = ('https://syr-res.com',
            'href="(https://syr-res.com/article/[0-9].*?.html)')

Website3 = ('http://n-scientific.org',
            'href="(http://n-scientific.org/[0-9].*?)"\s.*?</h3>')

# Lists of Tuples: Websites and their Regular Expressions
WEBlist = [Website1, Website2, Website3]

# Twitter Credentials:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Print Our Logo In The Terminal:
print('''\x1b[32m
██╗██╗     ███╗   ███╗    ███████╗███╗   ███╗
██║██║     ████╗ ████║    ██╔════╝████╗ ████║
██║██║     ██╔████╔██║    █████╗  ██╔████╔██║
██║██║     ██║╚██╔╝██║    ██╔══╝  ██║╚██╔╝██║
██║███████╗██║ ╚═╝ ██║    ██║     ██║ ╚═╝ ██║
╚═╝╚══════╝╚═╝     ╚═╝    ╚═╝     ╚═╝     ╚═╝
\x1b[0m''')

# Connecting To Twitter:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
print('\x1b[33m' + '[+] Connected To Twitter' + '\x1b[0m')
print('\x1b[35m' + '------------------------------' + '\x1b[0m')


'''Parses a website, gets all links that satisfy the given regular
expression with their titles, then returns a random tuple with link and the
page's title'''


def GetLink(Website, RegularExpression):
    web = urllib.request.urlopen(Website)
    URLs = list()
    for line in web:
        line = line.decode()
        article = re.findall(RegularExpression, line)
        if article == []:
            continue
        else:
            URLs.append(article[0])
    random.shuffle(URLs)
    URL = URLs[0]

    web = urllib.request.urlopen(URLs[0])
    for line in web:
        line = line.decode()
        article = re.findall('<title>(.*?)</title>', line)
        if article == []:
            continue
        else:
            TITLE = article[0]
    return(URL, TITLE)


'''Tweets a weblink and its title'''


def Tweet(TheWeb, TheRE):
    try:
        dateSTR = datetime.datetime.now().strftime('%H:%M')
        Result = GetLink(TheWeb, TheRE)
        TheTweet = Result[1] + '\n' + Result[0] + '\n' + '#علوم'
        api.update_status(TheTweet)
        print(
            '\x1b[34m' + '[+] Tweet at ' + dateSTR + '\x1b[0m' + '\n' +
            TheTweet + '\n')

    except Exception as TheError:
        print('\x1b[31m' + '[-] ERROR' + '\x1b[0m')
        print(TheError)


random.shuffle(WEBlist)
TheWebsite = WEBlist[0]
Tweet(TheWebsite[0], TheWebsite[1])
