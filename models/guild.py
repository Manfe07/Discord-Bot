from db import database

class Guild():
    id = 0
    guild_name = ""
    spam_channel_id = 0
    db = database()

    def __init__(self, id, db):
        self.id = id
        result = self.db.get_guild(id)
        if result != 0:
            data = result["data"]
            self.guild_name = data["guild_name"]
            self.spam_channel_id = data["channel_id"]
        else:
            self.save_to_db()

        self.db = db

    def save_to_db(self):
        data = {"channel_id" : self.spam_channel_id,
                "guild_name" : self.guild_name}
        self.db.update_guild(self.id, data)

    def set_channel_id(self, _channel_id):
        self.spam_channel_id = _channel_id
        self.save_to_db()
