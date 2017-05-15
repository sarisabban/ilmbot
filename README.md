# ilmbot

## Description:
This is a twitter bot specific for the Ilm FM science podcast's twitter account. The bot parses some science news websites in order to search for science articles. It then tweets a random link from the websites.

## How to Use:

1. Install Dependecies

```
pip3 install tweepy bs4 html5lib
```

2. Add the Twitter credentials to the keys.py file.
3. You can excute the script manually `python3 ilm.py`. But a more efficient way is to add the command as a cronjob.


## Configuration

To add a new website make a new variable containing a tuple under "Lists of Tuples" with the website's URL in the first position and the best way to identify article URLs using Regular Expression in the second position.

Next add your website tuple to the WEBlist under "Lists of Tuples".
