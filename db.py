from tinydb import TinyDB, Query
import discord

search_query = Query()

class database():

    db = TinyDB('data/database.json')

    def get_guild(self, id):
        result = self.db.search(search_query.id == id)
        if len(result) == 0:
            return 0
        else:
            return result[0]

    def update_guild(self, id, data : dict):
        self.db.update({'data': data}, search_query.id == id)

    def create_homework(self, guild_id, subject : str, task : str, date):
        self.db.table('homework').insert({'guild': guild_id, 'subject': subject, 'task': task, 'date': date})

    def get_homework(self, id):
        try:
            return self.db.table('homework').search(search_query.guild == id)
        except Exception:
            print(Exception)
            return []

if __name__ == "__main__":
    database = database()

    guild = database.get_guild(857637783946526720)
    print(guild)
