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
        if now.hour > 16 or now.hour < 6:
            await message.channel.send('Hab ich Bier gehört, ' + str(message.author.name) + '?😍')
            await message.channel.send('🍻')
        else:
            await message.channel.send('Kein Bier vor Vier 🕓')

client.run(secrets.discord_token)
