from .Database import MyDatabase

client = MyDatabase.get_instance().client

UserDatabase = client['user']