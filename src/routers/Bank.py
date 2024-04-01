from functools import lru_cache
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
import requests

from src import UserDatabase
from src.dependencies import check_Oauth2
from src.routers import API_KEY

router = APIRouter(prefix='/api/bank', dependencies=[Depends(check_Oauth2)])


TRANSACTIONS_URL = 'https://oauth.casso.vn/v2/transactions'

user_collection = UserDatabase['list-user']

@lru_cache
def get_transaction():
    header = {
        "Authorization": API_KEY.get_secret_value(),
        "Content-Type": "application/json"
    }
    response = requests.get(TRANSACTIONS_URL, headers=header)

    return response

def check_user_name(username: str) -> bool:
    
    return True

@router.get('/histories')
async def get_all_history():
    
    response = get_transaction()

    return JSONResponse(content=response.json())

@router.get('/history/{username}')
async def get_user_transaction(username: Annotated[str, 'username of User in minecraft']):
    transaction = get_transaction()