# ILM_FM_bot

## DESCRIPTION:
This is a twitter bot specific for the ILM.FM science podcast's twitter account where the bot parses some science news websites to search for science articles and then tweets the links at specific times.

## HOW TO USE:
To use follow these steps:

1. To add a new website make a new variable under "List of Websites" with the website's URL.
2. Find the best way to identify article URLs using Regular Expression, than make a new varibale under "Regular Expression of Each Website" and place the ergular expression in it. 
3. Add your website variable to the WEBlist and your Regular Expression variable to the RElist list both under "Lists of Websites and their Regular Expressions".
4. Make sure you have the correct consumer_key, consumer_secret, access_token, access_token_secret from Twitter.
5. Excute the script with python 3 and leave it running 24/7: `python3 ilm.py`
6. The script will tweet one tweet from each website in the list with 1 hour between tweets.
