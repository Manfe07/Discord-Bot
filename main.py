import random

import discord
import datetime
import secrets

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as ' + str(client.user))
    print("Servers:")
    for guild in client.guilds:
        print(guild)
    print("")

@client.event
async def on_message(message):
    print(str(message.author) + " postet in [" + str(message.channel) +"] : " + message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello 🖐 ' + str(message.author.name))

    elif "bier" in message.content or "Bier" in message.content:
        now = datetime.datetime.now()
        if(now.weekday() > 4) or (now.weekday() == 4 and now.hour > 13):
            await message.channel.send("Hoch die Hände🙌\n! **!!WOCHENENDE!!**")
        if now.hour >= 16 or now.hour < 6:
            r = random.randrange(0,10,1)
            print(r)
            if r == 7:
                await message.channel.send('@everyone! ' + str(message.author.name) + " gibt **Bier** aus!🍻")
            else:
                await message.channel.send('Hab ich **Bier** gehört, ' + str(message.author.name) + '?😍')
                await message.channel.send('🍻')
        else:
            await message.channel.send('Kein Bier vor Vier 🕓 😢')

client.run(secrets.discord_token)
