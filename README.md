# dad
Dad Bot is a little Discord bot with one purpose of simply being there just to entertain people with responses to certain phrases. This was my first project I've ever made.

If you don't want to self host this bot you can invite the copy that I personally host 24/7 with the bot invite
Bot invite: https://discord.com/oauth2/authorize?client_id=768028461670858752&permissions=67497024&scope=bot

How to set it up/self host:

1. This bot requires a specific version of Python. Download and install Python 3.8.3 from here https://www.python.org/downloads/release/python-383/

2. Create a bot account and get it's token (see this website): https://discordpy.readthedocs.io/en/latest/discord.html

3. Go to line 15 in bot.py and replace TOKEN_HERE with the bot token you just made (keep the " marks)

4. Go to config.ini (open it with a text editor) and add your discord ID (or multiple discord IDs seperated by a comma e.g. ID, ID)

4. cd into where your bot files are stored using cd PATH TO FOLDER and run the following command: pip install discord.py

4 1/2. If you need to install any more modules install them with pip

5. If you are on windows run python bot.py to start the bot

5 1/2. If you are on a UNIX based OS (macOS/Linux) run python3 bot.py to start the bot

This repo will be available on an as-is basis. Semi-rewriting the bot is already a stretch for me. I probably won't provide any more support for the bot unless it blows up even more than it already has.
