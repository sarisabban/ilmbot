# ILM_FM_bot

## DESCRIPTION:
This is a twitter bot specific for the ILM.FM science podcast's twitter account where the bot parses some science news websites to search for science articles and then tweets the links at specific times.

## HOW TO USE:

1. Install Dependecies

	pip3 install tweepy bs4 html5lib

2. Add the Twitter credentials to the keys.py file.
3. To add a new website make a new variable containing a tuple under "Lists of Tuples" with the website's URL in the first position and the best way to identify article URLs using Regular Expression in the second position.
4. Add your website tuple to the WEBlist under "Lists of Tuples".
5. Excute the script with python 3: `python3 ilm.py`
6. The script will tweet one random link from a randomly chosen website.
