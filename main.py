import random
import discord
import datetime
import secrets
from db import database
from models.guild import Guild


client = discord.Client()
db = database()
guilds = []

@client.event
async def on_ready():
    print('we have logged in as ' + str(client.user))
    print("Servers:")
    await client.change_presence(activity=discord.Game("BeerPong") ,status=discord.Status.online)
    for _guild in client.guilds:
        guilde = Guild(_guild.id, db)
        guilde.guild_name = str(_guild)
        guilds.append(guilde)
        guilde.save_to_db()
        print(guilde.guild_name)
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
            if r == 7:
                embed = discord.Embed(title='{} gibt Bier aus 🍻!!'.format(message.author.name),
                                      description='@everyone!\n<@{}> ist der glückliche Gewinner und darf jetzt jedem ein Bier ausgeben!'.format(message.author.id),
                                      colour=0xfcba03)
                #embed.add_field(name='Bier:', value='Veltins', inline=True)
                embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/761/761777.png")
                embed.add_field(name="Wann?",value="ab jetzt",inline=True)
                mes = await message.channel.send(embed=embed)
                await mes.add_reaction('🍻')
            else:
                await message.channel.send('Hab ich **Bier** gehört, ' + str(message.author.name) + '?😍')
                await message.channel.send('🍻')

        else:
            await message.channel.send('Kein Bier vor Vier 🕓 😢')

    #!join
    elif message.content.startswith('!join'):
        guild = Guild(message.guild.id,db)
        guild.set_channel_id(message.channel.id)
        await  message.channel.send('Ich arbeite jetzt im Channel {}'.format(message.channel.name))

    #!homework
    elif message.content.startswith('!homework'):
        content = message.content.split(',')
        print(content)
        if (len(content)) == 4:
            subject = content[1]
            tasks = content[2]
            date = content[3]
            await message.channel.send(tasks + " in/bei " + subject + " bis zum " + date)
        elif len(content) == 1:
            await message.channel.send("hier würden jetzt die Hausaufgaben stehen")
        else:
            await message.channel.send("Leider konnte ich deine eingabe für die Hausaufgaben verstehen😔\nVersuche es mit:\n`!homework, Fach, Aufgabe, Datum bis abgabe`")
client.run(secrets.discord_token)

