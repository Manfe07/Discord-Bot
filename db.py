from tinydb import TinyDB, Query
import discord

search_query = Query()

class database():

    db = TinyDB('data/database.json')

    def get_guild(self, id):
        result = self.db.table('guild').search(search_query.id == id)
        if len(result) == 0:
            self.db.table('guild').insert({'id': id})
            return 0
        else:
            return result[0]

    def update_guild(self, id, field : str, data):
        self.db.table('guild').upsert({field: data}, search_query.id == id)

    def create_homework(self, guild_id, subject : str, task : str, date):
        self.db.table('homework').insert({'guild': guild_id, 'subject': subject, 'task': task, 'date': date})

    def get_homework(self, id):
        try:
            return self.db.table('homework').search(search_query.guild == id)
        except Exception as e:
            print(e)
            return []

    def del_homework(self, id, date_time : str):
        try:
            self.db.table('homework').remove(search_query.date == date_time)
        except Exception as e:
            print(e)
