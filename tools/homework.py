import datetime

import discord
from db import database
import tools.str_tools as str_tools

async def handle_message(message : discord.Message, db : database):
    content = message.content.split(',')
    if (len(content)) == 4:
        await save_homework(message, db)

    elif len(content) == 1:
        await print_homework(message, db)
    else:
        await message.channel.send("Leider konnte ich deine eingabe für die Hausaufgaben verstehen😔\nVersuche es mit:\n`!homework, Fach, Aufgabe, Datum bis abgabe`")

async def save_homework(message : discord.Message, db : database):
    content = message.content.split(',')
    subject = str_tools.remove_first_space(content[1])
    task = str_tools.remove_first_space(content[2])
    date = str_tools.remove_first_space(content[3])
    # date = datetime.datetime.strptime(content[3], '%d.%m.%y')
    print(date)
    db.create_homework(message.guild.id, subject, task, date)
    await message.channel.send(task + " in/bei " + subject + " bis zum " + date)

async def print_homework(message : discord.Message, db : database):
    homework_list = db.get_homework(message.guild.id)
    print(homework_list)
    print(homework_list)
    if len(homework_list) > 0:
        for homework in homework_list:
            subject = homework["subject"]
            task = homework["task"]
            date = homework["date"]
            date_split = date.split(".")
            stamp = datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0]))
            if stamp < datetime.datetime.now().date():
                db.del_homework(message.guild.id,date)
            else:
                await message.channel.send("`" + task + "` in/bei `" + subject + "` bis zum `" + stamp.strftime('%d.%m.%y') + "`")
    else:
        await message.channel.send("Keine Hausaufgaben 🎉")