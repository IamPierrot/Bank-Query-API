from dotenv import dotenv_values, load_dotenv
from pydantic import SecretStr


load_dotenv('.env')


API_KEY = SecretStr(dotenv_values('.env')['API_KEY'])
ACCESS_TOKEN = SecretStr(dotenv_values('.env')['TOKEN'])