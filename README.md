# ILM_FM_bot

## DESCRIPTION:
This is a twitter bot specific for the ILM.FM science podcast's twitter account where the bot parses some science news websites to search for science articles and then tweets the links at specific times.

## HOW TO USE:
To use follow these steps:

1. To add a new website make a new variable containing a tuple under "Lists of Tuples" with the website's URL in the first position and the best way to identify article URLs using Regular Expression in the second position.
2. Add your website tuple to the WEBlist under "Lists of Tuples".
3. Make sure you have the correct consumer_key, consumer_secret, access_token, access_token_secret from Twitter.
4. Excute the script with python 3: `python3 ilm.py`
5. The script will tweet one random link from a randomly chosen website.
