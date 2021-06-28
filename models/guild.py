from db import database

class Guild():
    id = 0
    guild_name = ""
    spam_channel_id = 0
    db = database()

    def __init__(self, id, db):
        self.id = id
        self.db = db
        data = self.db.get_guild(id)
        try:
            self.spam_channel_id = data["channel_id"]
        except Exception as e:
            print(e)

    def save_to_db(self):
        self.db.update_guild(self.id, "channel_id", self.spam_channel_id)

    def set_channel_id(self, _channel_id):
        self.spam_channel_id = _channel_id
        self.db.update_guild(self.id, "channel_id", self.spam_channel_id)

    def set_guild_name(self, _guildName):
        self.guild_name = _guildName
        self.db.update_guild(self.id, "guild_name", self.guild_name)
