# CPU Purple Heart

![Nep Nep](https://caboosh.s-ul.eu/NpVgetoh.png)

The Lovable CPU of Planeptune has smashed the 4th wall hard enough to make it onto discord somehow, don't ask me how, she just did, alrite?

# Setup and botconfig making
## Requirements:
- discord.py rewrite (1.0.0a)
- Latest version of Python

## Installing
- Refer to wiki for installation

## Botconfig.py file
This file should contain 3 variables as of now, "token" , "prefix" , and "botdesc".
These varables are imported in the main bot.py as to allow somewhat dynamic changing of these (desc and prefix) elements through either the bot or just by editing the botconfig.py file. 

basically, the botconfig.py should look like this:
```python
import datetime

botversion = 'The Version of the bot (May be different if you are using a personal fork)'
since = datetime.datetime('Year', 'Month', 'Day')
prefix = 'Enter your Prefix here'
token = 'Put your token here'

botdesc = '''The Description of the bot if being used for other uses apart from being Nep'''
``` 

## Statuses and other bits

[![Documentation Status](http://readthedocs.org/projects/cpu-purple-heart/badge/?version=latest)](http://cpuneptune.cameronmiller.me/?badge=latest)
