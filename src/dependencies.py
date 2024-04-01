from typing import Annotated

from fastapi import Header

from src.models.ErrorModel import AuthorizedException
from src.routers import ACCESS_TOKEN


def check_Oauth2(access_token: Annotated[str | None, Header()] = None):
    if access_token is None or access_token != ACCESS_TOKEN.get_secret_value():
        raise AuthorizedException(missing=["access-token"] if access_token is None else [])
    pass