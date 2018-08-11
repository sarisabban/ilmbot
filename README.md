# ilmbot
A Twitter bot for the twitter account of my podcast ILM FM:

## Website:
http://ILM.FM

## Description:
This is a twitter bot specific for the ILM FM science podcast's twitter account. The bot parses some science news websites in order to search for science articles. It then tweets a random link from the websites. The bot is designed to work on Debian based linux destributions.

## How to Use:
1. Install Dependecies

`sudo apt update && sudo apt full-upgrade && sudo apt install python-beautifulsoup python-lxml python-tweepy`

2. Add the Twitter credentials to the keys.py file.
3. You can excute the script manually `python ilm.py`. But a more efficient way is to setup a crons job (times are in UTC):

`crontab -e`

`
32 17 * * * python3 ilm.py >> ilm_Log 2>&1
12 18 * * * python3 ilm.py >> ilm_Log 2>&1
03 19 * * * python3 ilm.py >> ilm_Log 2>&1
08 20 * * * python3 ilm.py >> ilm_Log 2>&1
`

## Configuration
1. To add a new website make a new variable containing a tuple under "#Tuples of websites and their regular expressions" with the website's URL in the first position and the best way to identify article URLs using regular expression in the second position.
2. Next add your website's tuple to the WEBlist list under "Lists of tuples".
