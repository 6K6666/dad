# import all the shizz

import discord, time, pickle, random, os, sys, json
from configparser import ConfigParser

# bot variables & configs

config = ConfigParser()  
client = discord.Client()
config.read('config.ini')
locked = config.get('settings', 'locked')
admin = config.get('settings', 'admin')
status1213 = discord.Streaming(name="Run 'help", url="https://www.youtube.com/watch?v=iU9V4FEG_D4")
prefix = "'" # bot prefix, set to ' by default
token = ("TOKEN_HERE") # replace TOKEN_HERE with your bot token generated from the discord developer page (IMPORTANT!!!)
gay = {}
pp = {}
try:
    with open("gay.pickle", 'rb') as f:
        gay = pickle.load(f)
except:
    pass
try:
    with open("pp.pickle", 'rb') as f:
        pp = pickle.load(f)
except:
    pass

# Startup

@client.event 
async def on_ready():
    print(("I am running on " + client.user.name))
    print(("With the ID: " + str(client.user.id)))
    guilds=list(client.guilds)
    print("connected on " + str(len(client.guilds)) + " servers:")
    for x in range(len(guilds)):
        print('  '+ guilds[x-1].name)
    time.sleep(5)
    await client.change_presence(activity=status1213)

# Welcome message

@client.event
async def on_guild_join(guild): # I joined something new!!!
    channel = sorted([chan for chan in guild.channels if 
        chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
    embed=discord.Embed(title="Dad", color=0x0000ff, description="Hi! My name is Dad, thanks for inviting me here. Run " + prefix + "help to see all my commands. Oh, also, my code is open source, too! If you want to take a look at my source code you can do so at https://github.com/6K6666/dad")
    await channel.send(embed=embed)

# Admin only commands

@client.event
async def on_message(message):

    user_message = str(message.content) # using this allows us to tolower and ignore case on some commands

    if message.content.lower() == prefix + 'lock': # Lock the bot from being used
        print('checking user permissions')
        if str(message.author.id) in admin:
            print('permissions validated')
            if locked == "False":
                await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Bot locked down by a bot admin!"))
                print('locked down')
                with open('config.ini', 'w') as configfile:
                    config.read('config.ini')
                    config.set('settings', 'locked', 'True')
                    config.write(configfile)
                    embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is now locked down!")
                    await message.channel.send(embed=embed)
            elif locked == "True":
                embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is already locked, you can unlock him by using the unlock command")
                await message.channel.send(embed=embed)
    
    if message.content.lower() == prefix + 'unlock': # Unlock the bot
        print('checking user permissions')
        if str(message.author.id) in admin:
            print('permissions validated')
            if locked == "True":
                await client.change_presence(activity=status1213)
                print('unlocked')
                with open('config.ini', 'w') as configfile:
                    config.read('config.ini')
                    config.set('settings', 'locked', 'False')
                    config.write(configfile)
                    embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is now unlocked")
                    await message.channel.send(embed=embed)
            elif locked == "False":
                embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is already unlocked, you can lock him by using the lock command")
                await message.channel.send(embed=embed)

    if user_message.lower() == prefix + 'restart': # Restart the bot
        if str(message.author.id) in admin:
            await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Restarting..."))
            embed=discord.Embed(title="Dad", color=0x0000ff)
            embed.add_field(name="Restarting...", value="Restarting discord bot.", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(8)
            os.system("python bot.py")
            sys.exit()
        else:
            embed=discord.Embed(title="Dad", color=0xff0000, description="You're not a bot admin.")
            await message.channel.send(embed=embed)

    if user_message.lower() == prefix + 'shutdown': # Shuts down the bot
        if str(message.author.id) in admin:
            await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Shutting down..."))
            embed=discord.Embed(title="Dad", color=0x0000ff)
            embed.add_field(name="Shutting down...", value="Shutting down discord bot.", inline=False)
            await message.channel.send(embed=embed)
            sys.exit()
        else:
            embed=discord.Embed(title="Dad", color=0xff0000, description="You're not a bot admin.")
            await message.channel.send(embed=embed)
    
    if user_message.lower() == prefix + 'sc': # Server count
        if str(message.author.id) in admin:
            await message.channel.send("Currently in " + str(len(client.guilds)) + " servers")
        else:
            embed=discord.Embed(title="Dad", color=0xff0000, description="You're not a bot admin.")
            await message.channel.send(embed=embed)
    
    # user facing commands

    if user_message.lower() == prefix + 'ping': # Ping command
        if locked == "True":
            return
        latency = client.latency
        await message.channel.send('My current latency is ' + str(client.latency))

    if user_message.lower() == prefix + 'flip': # Coinflip
        if locked == "True":
            return
        flipper = random.randrange(1,3)
        if flipper == 1:
            embed=discord.Embed(title="Dad", color=0x0000ff, description="Heads!")
            await message.channel.send(embed=embed)
        if flipper == 2:
            embed=discord.Embed(title="Dad", color=0x0000ff, description="Tails!")
            await message.channel.send(embed=embed)

    if user_message.lower() == prefix + 'help': # Help menu
        if locked == "True":
            if message.author == client.user:
                return
        embed=discord.Embed(title="A list of commands has been sent to your DMs!", color=0x0000ff, description="If you didn't recieve a DM be sure your privacy settings aren't blocking the message from being sent.")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="", color=0x0000ff)
        embed.add_field(name="Dad's command list", value="Message a bot admin if you require support.", inline=False)
        embed.add_field(name="_ _", value="_ _", inline=False)
        embed.add_field(name= prefix + "help", value="The thing you're looking at", inline=False)
        embed.add_field(name= prefix + "ping", value="Shows the current latency for Dad Bot", inline=False)
        embed.add_field(name= prefix + "avatar", value="Shows your avatar (does not work to show others at this time)", inline=False)
        embed.add_field(name= prefix + "invite", value="Sends the discord bot invite link so you can invite Dad Bot to more servers", inline=False)
        embed.add_field(name= prefix + "vote", value="Vote for our bot on these sites so Dad can grow", inline=False)
        embed.add_field(name= prefix + "pp <person place or thing>", value="Measures someone's pp", inline=False)
        embed.add_field(name= prefix + "gay <person place or thing>", value="Measures how gay someone is", inline=False)
        embed.add_field(name= prefix + "flip", value="Flip a coin, heads or tails", inline=False)
        embed.add_field(name= prefix + "8ball <is dad gay>", value="Its 8ball, everyone knows what it is", inline=False)
        embed.add_field(name= prefix + "toggleprank", value="Toggles the Hi cool, I'm dad! thing (requires manage server perms)", inline=False)
        embed.add_field(name= prefix + "togglewalter", value="Toggles the walter feature (requires manage server perms)", inline=False)
        embed.add_field(name= prefix + "toggleanticancer", value="Toggles the module which deletes cancerous things like i- and oop- and responds with something toxic (requires manage server perms)", inline=False)
        embed.add_field(name="_ _", value="_ _", inline=False)
        embed.add_field(name="Bot admins", value="Ownership of apl#1001, 6K#6666, Roka#1337 and reknohT#6536. This is a rewritten version of Dad Bot. Please let bot admins know if there are any issues with the bot.", inline=False)
        await message.author.send(embed=embed)
    
    if user_message.lower() == prefix + 'invite': # Bot invite
        if locked == "False":
            embed=discord.Embed(title="Dad", color=0x0000ff)
            embed.add_field(name="Invite Dad Bot to your servers with this link", value="https://discord.com/oauth2/authorize?client_id=768028461670858752&permissions=67497024&scope=bot", inline=False)
            await message.channel.send(embed=embed)

    #if user_message.lower() == prefix + 'vote':   ------ commented out because both of these links are dead
        #if locked == "False":
            #embed=discord.Embed(title="Support Dad Bot by voting!", color=0x0000ff)
            #embed.add_field(name="Upvote on top.gg", value="https://top.gg/bot/739399686284115990", inline=False)
            #embed.add_field(name="Upvote on Discord Extreme List", value="https://discordextremelist.xyz/en-US/bots/dad", inline=False)
            #await message.channel.send(embed=embed)

    # case sensitive commands, relatively unchanged in the rewrite

    if message.author.id == client.user.id or "@" in message.content or "http" in message.content == "True": ## Prevents the bot from responding to itself and people from misusing commands
        return

    if message.content.startswith(prefix + "gay"): # Gay, case sensitive
        if locked == "False":
            messagee = message.content[len(prefix + "gay"):].strip()
            if not messagee:
                return
            if messagee in gay:
                embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " is {}% gay".format(gay[messagee]))
                await message.channel.send(embed=embed)
            else:
                gay[messagee] = str(random.randrange(0,101))
                with open("gay.pickle", 'wb') as f:
                    pickle.dump(gay, f)
                embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " is {}% gay".format(gay[messagee]))
                await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "pp"): # pp size command, case sensitive
        if locked == "False":
            messagee = message.content[len(prefix + "pp"):].strip()
            if not messagee:
                return
            if messagee in pp:
                if pp[messagee] == 0: # no pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has no pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 1: # very small pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a very small pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 2: # small pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a small pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 3: # big pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a big pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 4: # very big pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a very big pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 5: # Gigantic pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a gigantic pp.")
                    await message.channel.send(embed=embed)
            else:
                pp[messagee] = random.randrange(0,5)
                with open("pp.pickle", 'wb') as f:
                    pickle.dump(pp, f)
                if pp[messagee] == 0: # no pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has no pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 1: # very small pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a very small pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 2: # small pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a small pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 3: # big pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a big pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 4: # very big pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a very big pp.")
                    await message.channel.send(embed=embed)
                elif pp[messagee] == 5: # Gigantic pp
                    embed=discord.Embed(title="Dad", color=0x0000ff, description=messagee + " has a gigantic pp.")
                    await message.channel.send(embed=embed)

    if message.content.startswith(prefix + "8ball"): # 8-ball command
        if locked == "False":
            messagee = message.content[len(prefix + "8ball"):].strip()
            if not message:
                return
            ateball = random.randrange(1,22)
            if ateball == 1:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="It is certain.")
                await message.channel.send(embed=embed)
            if ateball == 2:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="It is decidedly so.")
                await message.channel.send(embed=embed)
            if ateball == 3:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Without a doubt.")
                await message.channel.send(embed=embed)
            if ateball == 4:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Yes - definitely.")
                await message.channel.send(embed=embed)
            if ateball == 5:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="As I see it, yes.")
                await message.channel.send(embed=embed)
            if ateball == 6:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Most likely.")
                await message.channel.send(embed=embed)
            if ateball == 7:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Outlook good.")
                await message.channel.send(embed=embed)
            if ateball == 8:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Yes.")
                await message.channel.send(embed=embed)
            if ateball == 9:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="Signs point to yes.")
                await message.channel.send(embed=embed)
            if ateball == 10:
                embed=discord.Embed(title="Dad", color=0x00ff00, description="You may rely on it.")
                await message.channel.send(embed=embed)
            if ateball == 11:
                embed=discord.Embed(title="Dad", color=0xffff00, description="Reply hazy, try again.")
                await message.channel.send(embed=embed)
            if ateball == 12:
                embed=discord.Embed(title="Dad", color=0xffff00, description="Ask again later.")
                await message.channel.send(embed=embed)
            if ateball == 13:
                embed=discord.Embed(title="Dad", color=0xffff00, description="Better not tell you now.")
                await message.channel.send(embed=embed)
            if ateball == 14:
                embed=discord.Embed(title="Dad", color=0xffff00, description="Cannot predict now.")
                await message.channel.send(embed=embed)
            if ateball == 15:
                embed=discord.Embed(title="Dad", color=0xffff00, description="Concentrate and ask again.")
                await message.channel.send(embed=embed)
            if ateball == 16:
                embed=discord.Embed(title="Dad", color=0xff0000, description="Don't count on it.")
                await message.channel.send(embed=embed)
            if ateball == 17:
                embed=discord.Embed(title="Dad", color=0xff0000, description="My reply is no.")
                await message.channel.send(embed=embed)
            if ateball == 18:
                embed=discord.Embed(title="Dad", color=0xff0000, description="My sources say no.")
                await message.channel.send(embed=embed)
            if ateball == 19:
                embed=discord.Embed(title="Dad", color=0xff0000, description="Outlook not so good.")
                await message.channel.send(embed=embed)
            if ateball == 20:
                embed=discord.Embed(title="Dad", color=0xff0000, description="Very doubtful.")
                await message.channel.send(embed=embed)
            if ateball == 21:
                embed=discord.Embed(title="Dad", color=0xff0000, description="Ask joe.")
                await message.channel.send(embed=embed)
            if ateball == 22:
                embed=discord.Embed(title="Dad", color=0xff0000, description="lmao yea")
                await message.channel.send(embed=embed)  

    # Auto responders, also unchanged

    with open('joe.json', 'r') as f: # walter and reknoht auto responders
       data = json.load(f)
    if locked == "False":
        if message.guild.id not in data["walter"]:
            if message.content.startswith('STOP'):
                await message.channel.send('walter')
            if 'walter' in message.content or message.content.startswith('i like fire trucks and moster trucks'):
                await message.channel.send('walter')
            if 'Walter' in message.content or message.content.startswith('I like fire trucks and moster trucks'):
                await message.channel.send('walter')
            if 'WALTER' in message.content or message.content.startswith('I LIKE FIRE TRUCKS AND MOSTER TRUCKS'):
                await message.channel.send('walter')
            if message.content.startswith('i like fire trucks'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653382886145392652/91.png')
            if message.content.startswith('I LIKE FIRE TRUCKS'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653382886145392652/91.png')
            if message.content.startswith('I like fire trucks'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653382886145392652/91.png')
            if message.content.startswith('i like moster trucks'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653383291491319839/Batman_truck-e1509637628994.png')
            if message.content.startswith('I like moster trucks'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653383291491319839/Batman_truck-e1509637628994.png')          
            if message.content.startswith('I LIKE MOSTER TRUCKS'):
                await message.channel.send('https://cdn.discordapp.com/attachments/640715239779860500/653383291491319839/Batman_truck-e1509637628994.png')
            if message.content.startswith('i like reknohT'):
                await message.channel.send('https://cdn.discordapp.com/attachments/658736872906031104/727663065604292608/reknoht.jpg')
            rand = random.randrange(1,500)
            if rand == 69:
                await message.channel.send('i like fire trucks and moster trucks')

    with open('joe.json', 'r') as f: # Hi ___, I'm Dad auto responder
       data = json.load(f)
    if locked == "False":
        if message.guild.id not in data["prank"]:
            if message.content.startswith("i'm ") or message.content.startswith("im ") or message.content.startswith("I'm ") or message.content.startswith("Im "): 
                if message.content.startswith("i'm"):
                    name = message.content[len("i'm"):].strip()
                elif message.content.startswith("im"):
                    name = message.content[len("im"):].strip()
                elif message.content.startswith("I'm"):
                    name = message.content[len("I'm"):].strip()
                elif message.content.startswith("Im"):
                    name = message.content[len("Im"):].strip()
                if not name or "http" in name or "@" in name or "@" in name:
                    return
                await message.channel.send("Hi " + name + ", I\'m Dad!")
    
    with open('joe.json', 'r') as f:
       data = json.load(f) # anti cancer 
    if locked == "False":
            if message.guild.id not in data["anticancer"]:
                if 'I-' in message.content or message.content.startswith('I-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'i-' in message.content or message.content.startswith('i-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'and i oop' in message.content or message.content.startswith('and i oop'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'AND I OOP' in message.content or message.content.startswith('AND I OOP'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'oop-' in message.content or message.content.startswith('oop-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'Oop-' in message.content or message.content.startswith('Oop-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'OOP-' in message.content or message.content.startswith('OOP-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'OOp-' in message.content or message.content.startswith('OOp-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'periodt' in message.content or message.content.startswith('periodt'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'PERIODT' in message.content or message.content.startswith('PERIODT'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')
                if 'Periodt' in message.content or message.content.startswith('Periodt'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:768033299217252363> <:rtole:768033299565641738>')

    
    # disable commands locally

    if user_message.lower() == prefix + 'toggleprank': # Disabled prank locally
        if message.author.guild_permissions.manage_guild == True:
            with open('joe.json', 'r') as f:
              data = json.load(f)
              if message.guild.id in data["prank"]:
                data["prank"].remove(message.guild.id)
                await message.channel.send("Toggled on")
              elif message.guild.id not in data["prank"]:
                data["prank"].append(message.guild.id)
                await message.channel.send("Toggled off")
            with open('joe.json', 'w') as f:
              json.dump(data, f, indent=4)
        if message.author.guild_permissions.manage_guild == False:
            return await message.channel.send("You're missing manage server permissions")

    if user_message.lower() == prefix + 'togglewalter': # Disabled walter locally
        if message.author.guild_permissions.manage_guild == True:
            with open('joe.json', 'r') as f:
              data = json.load(f)
              if message.guild.id in data["walter"]:
                data["walter"].remove(message.guild.id)
                await message.channel.send("Toggled on")
              elif message.guild.id not in data["walter"]:
                data["walter"].append(message.guild.id)
                await message.channel.send("Toggled off")
            with open('joe.json', 'w') as f:
              json.dump(data, f, indent=4)
        elif message.author.guild_permissions.manage_guild == False:
            return await message.channel.send("You're missing manage server permissions")

    if user_message.lower() == prefix + 'toggleanticancer': # Disabled anti cancer locally
        if message.author.guild_permissions.manage_guild == True:
            with open('joe.json', 'r') as f:
              data = json.load(f)
              if message.guild.id in data["anticancer"]:
                data["anticancer"].remove(message.guild.id)
                await message.channel.send("Toggled on")
              elif message.guild.id not in data["anticancer"]:
                data["anticancer"].append(message.guild.id)
                await message.channel.send("Toggled off")
            with open('joe.json', 'w') as f:
              json.dump(data, f, indent=4)
        elif message.author.guild_permissions.manage_guild == False:
            return await message.channel.send("You're missing manage server permissions")
    
client.run(token) # runs the bot with the provided token in the token variable
