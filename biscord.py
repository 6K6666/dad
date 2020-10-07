import discord, random, pickle, sys, os.path, json, os, time
from configparser import ConfigParser
from discord.utils import find
from itertools import cycle
from discord.ext import commands, tasks
from discord.ext.commands import Bot
config = ConfigParser()  
client = discord.Client()
config.read('config.ini')
keybind = "'" # Prefix owo
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


@client.event # Startup
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Starting...")) 
    print(("I am running on " + client.user.name))
    print(("With the ID: " + str(client.user.id)))
    guilds=list(client.guilds)
    print("connected on " + str(len(client.guilds)) + " servers:")
    for x in range(len(guilds)):
        print('  '+ guilds[x-1].name)
    time.sleep(5)
    await client.change_presence(activity=discord.Streaming(name="Run 'help", url="https://www.youtube.com/watch?v=iU9V4FEG_D4"))


@client.event
async def on_message(message):
    muted = config.get('settings', 'mute')
    admin = config.get('settings', 'admin')
    prank = config.get('settings', 'prank')
    black = config.get('settings', 'blacklist')
    walter = config.get('settings', 'walter')
    if str(message.author.id) in black:
        return  
    if message.content.startswith(keybind + "gtogglemute"): # Mute the bot globally (depreciated, might not mute all bot functions)
        if str(message.author.id) in admin:
            if muted == "False":
                await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Bot locked down by a bot admin!"))
                print('muted')
                with open('config.ini', 'w') as configfile:
                    config.read('config.ini')
                    config.set('settings', 'mute', 'True')
                    config.write(configfile)
                    embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is now muted!")
                    await message.channel.send(embed=embed)
            elif muted == "True":
                print('Unmuted')
                with open('config.ini', 'w') as configfile:
                    config.read('config.ini')
                    config.set('settings', 'mute', 'False')
                    config.write(configfile)
                    embed=discord.Embed(title="Dad", color=0x0000ff, description="Dad is now unmuted!")
                    await message.channel.send(embed=embed)
                await client.change_presence(activity=discord.Streaming(name="Run 'help", url="https://www.youtube.com/watch?v=iU9V4FEG_D4"))
        else:
            embed=discord.Embed(title="Dad", color=0xff0000, description="You're not cool. Try again later")
            await message.channel.send(embed=embed)
    if str(message.author.id) in black or message.author.id == client.user.id or "@" in message.content or "@" in message.content or muted == "True":
        return
    
    if message.content.startswith(keybind + "flip"): # coin flip
        if muted == "False": 
            flipper = random.randrange(1,3)
            if flipper == 1:
                embed=discord.Embed(title="Dad", color=0x0000ff, description="Heads!")
                await message.channel.send(embed=embed)
            if flipper == 2:
                embed=discord.Embed(title="Dad", color=0x0000ff, description="Tails!")
                await message.channel.send(embed=embed)

    if message.content.startswith(keybind + "help"): # Help!!! dick stuck in toaster
        if muted == "False":
            if message.author == client.user:
                return
        embed=discord.Embed(title="A list of commands has been sent to your DMs!", color=0x0000ff, description="If you didn't recieve a DM be sure your privacy settings aren't blocking the message from being sent. ")
        await message.channel.send(embed=embed)
        embed=discord.Embed(title="", color=0x0000ff)
        embed.add_field(name="Dad's command list", value="Message the bot developer if you require support", inline=False)
        embed.add_field(name="'help", value="The thing you're looking at", inline=False)
        embed.add_field(name="'invite", value="Sends the discord bot invite link so you can invite Dad Bot to more servers", inline=False)
        embed.add_field(name="'pp <person place or thing>", value="Measures someone's pp", inline=False)
        embed.add_field(name="'gay <person place or thing>", value="Measures how gay someone is", inline=False)
        embed.add_field(name="'flip", value="Flip a coin, heads or tails", inline=False)
        embed.add_field(name="'8ball <is dad gay>", value="Its 8ball, everyone knows what it is", inline=False)
        embed.add_field(name="'toggleprank", value="Toggles the Hi cool, I'm dad! thing (requires manage server perms)", inline=False)
        embed.add_field(name="'togglewalter", value="Toggles the walter feature (requires manage server perms)", inline=False)
        embed.add_field(name="'togglejoe", value="Toggles the joe mama responses (requires manage server perms)", inline=False)
        embed.add_field(name="'toggleanticancer", value="Toggles the module which deletes cancerous things like i- and oop- and responds with something toxic (requires manage server perms)", inline=False)
        await message.author.send(embed=embed)
        
    if message.content.startswith(keybind + "restart"): # Rebooting bot, HOOOOOOOOOOOOOOOOLD!
        if str(message.author.id) in admin:
            await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Restarting..."))
            embed=discord.Embed(title="Dad", color=0x0000ff)
            embed.add_field(name="Restarting...", value="Restarting discord bot.", inline=False)
            await message.channel.send(embed=embed)
            time.sleep(8)
            sys.exit()
        else:
            embed=discord.Embed(title="Dad", color=0xff0000, description="You're not a bot admin, trololo.")
            await message.channel.send(embed=embed)

    if message.content.startswith(keybind + "invite"): # Bot invite
        if muted == "False":
            embed=discord.Embed(title="Dad", color=0x0000ff)
            embed.add_field(name="Invite Dad Bot to your servers with this link", value="invite link not set by bot developer", inline=False)
            await message.channel.send(embed=embed) 

    if message.content.startswith(keybind + "gay"): # Gay!!!
        if muted == "False":
            messagee = message.content[len(keybind + "gay"):].strip()
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

    if message.content.startswith(keybind + "sc"): # How many servers am I in...
        await message.channel.send("connected on " + str(len(client.guilds)) + " servers")

    if message.content.startswith(keybind + "pp"): # Selfbot pp big!
        if muted == "False":
            messagee = message.content[len(keybind + "pp"):].strip()
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

    if message.content.startswith(keybind + "8ball"): # 8-ball nigga
        if muted == "False":
            messagee = message.content[len(keybind + "8ball"):].strip()
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
    
    with open('joe.json', 'r') as f:
       data = json.load(f)
    if walter == "True": # Walter 
        if muted == "False":
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
                if message.content.startswith('i like beyonce'):
                    await message.channel.send('https://cdn.discordapp.com/attachments/737057548863275018/739406855960264724/image0.png')
                if message.content.startswith('i like seasoning'):
                    await message.channel.send('https://cdn.discordapp.com/attachments/726213146628587600/739579570705137694/unknown.png')
                if message.content.startswith('i like reknohT'):
                    await message.channel.send('https://cdn.discordapp.com/attachments/658736872906031104/727663065604292608/reknoht.jpg')
                rand = random.randrange(1,500)
                if rand == 69:
                    await message.channel.send('i like fire trucks and moster trucks')

    with open('joe.json', 'r') as f:
       data = json.load(f)
    if prank == "True":
        if muted == "False":
            if message.guild.id not in data["prank"]:
                if message.content.startswith("i'm ") or message.content.startswith("im ") or message.content.startswith("I'm ") or message.content.startswith("Im "): # Im dad! owo
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
    if muted == "False":
            if message.guild.id not in data["anticancer"]:
                if 'I-' in message.content or message.content.startswith('I-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'i-' in message.content or message.content.startswith('i-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'and i oop' in message.content or message.content.startswith('and i oop'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'AND I OOP' in message.content or message.content.startswith('AND I OOP'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'oop-' in message.content or message.content.startswith('oop-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'Oop-' in message.content or message.content.startswith('Oop-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'OOP-' in message.content or message.content.startswith('OOP-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'OOp-' in message.content or message.content.startswith('OOp-'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'periodt' in message.content or message.content.startswith('periodt'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'PERIODT' in message.content or message.content.startswith('PERIODT'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')
                if 'Periodt' in message.content or message.content.startswith('Periodt'):
                    await message.delete()
                    await message.channel.send(f'{message.author.mention} DRAIN THE SWAMP!!! <:gape:742158646569468034> <:rtole:742158654249107526>')


    with open('joe.json', 'r') as f:
       data = json.load(f)
    if muted == "False": 
            if message.guild.id not in data["joes"]:
                if 'joe' in message.content or message.content.startswith('joe'):
                    await message.channel.send('joe mama')
                if 'Joe' in message.content or message.content.startswith('Joe'):
                    await message.channel.send('joe mama')
                if 'JOE' in message.content or message.content.startswith('JOE'):
                    await message.channel.send('joe mama')
                if 'JOe' in message.content or message.content.startswith('JOe'):
                    await message.channel.send('joe mama')
                if 'jOe' in message.content or message.content.startswith('jOe'):
                    await message.channel.send('joe mama')
                if 'jOE' in message.content or message.content.startswith('jOE'):
                    await message.channel.send('joe mama')
                if 'JoE' in message.content or message.content.startswith('JoE'):
                    await message.channel.send('joe mama')              

    if message.content.startswith(keybind + "echo"): # Repeat after me!
            if str(message.author.id) in admin:
                await message.channel.send(message.content[5:].format(message))
            else:
                embed=discord.Embed(title="Dad", color=0xff0000, description="You're not a bot admin, trololo.")
                await message.channel.send(embed=embed)
    
    if message.content.startswith(keybind + "toggleprank"): # Disabled prank locally
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

    if message.content.startswith(keybind + "togglejoe"): # Disabled prank locally
        if message.author.guild_permissions.manage_guild == True:
            with open('joe.json', 'r') as f:
              data = json.load(f)
              if message.guild.id in data["joes"]:
                data["joes"].remove(message.guild.id)
                await message.channel.send("Toggled on")
              elif message.guild.id not in data["joes"]:
                data["joes"].append(message.guild.id)
                await message.channel.send("Toggled off")
            with open('joe.json', 'w') as f:
              json.dump(data, f, indent=4)
        if message.author.guild_permissions.manage_guild == False:
            return await message.channel.send("You're missing manage server permissions")

    if message.content.startswith(keybind + "togglewalter"): # Disabled walter locally
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

    if message.content.startswith(keybind + "toggleanticancer"): # Disabled anti cancer locally
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

client.run('TOKEN HERE') 