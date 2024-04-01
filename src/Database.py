from pymongo import MongoClient
from dotenv import dotenv_values, load_dotenv

load_dotenv()
class MyDatabase:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MyDatabase()
        return cls._instance

    def __init__(self) -> None:
        if MyDatabase._instance is not None:
            raise Exception("This class is only created once!")
        self._URI = dotenv_values('.env')["DATABASE"]
        self.__connect_mongoDB__()

    def __connect_mongoDB__(self):
        try:
            self.client = MongoClient(host=self._URI)
        except Exception as e:
            raise Exception("Can not connect to database! Try again...", e)
        finally:
            print('✅ Successfully connect to database!')

if __name__ == "__main__":
    print(dotenv_values('.env'))