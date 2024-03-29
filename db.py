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

if __name__ == "__main__":
    database = database()

    guild = database.get_guild(857637783946526720)
    print(guild)
