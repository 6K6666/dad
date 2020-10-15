# dad
Dad Bot is a little Discord bot with one purpose of simply being there just to entertain people with responses to certain phrases. This was my first project I've ever made.


How to set it up:

1. This bot requires a special version of Python. Download and install Python 3.8.3 from here https://www.python.org/downloads/release/python-383/

2. Create a bot account and get it's token (see this website): https://discordpy.readthedocs.io/en/latest/discord.html

3. Go to line 438 in biscord.py and replace TOKEN HERE with the bot token you just made (keep the ' marks)

4. Go to config.ini (open it with a text editor) and paste the Discord token in the discordusername field and paste your Discord ID in the admin field and put your discord ID in the admins field

4. cd into where your bot files are stored using cd PATH TO FOLDER and run the following command: pip install discord.py

5. This step differs if you have a UNIX based OS (linux or macOS) or if you have Windows. To start the bot on Windows run start.bat and you're good to go. To start the bot on a UNIX based OS open a terminal window and run python3 biscord.py 

This repo will be available on an as-is basis. I won't be providing support for it or maintaining it anymore. You're free to do whatever you want with the source code, and I really do not care if you credit me or not for it. 
