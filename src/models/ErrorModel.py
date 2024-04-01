from fastapi import status


class AuthorizedException(Exception):
    def __init__(self, missing: list[str] = []) -> None:
        self.content = {
            "detail": "Unauthorized access token. Please contact to dev!",
            "missing_required": missing
        }
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.headers = {"WWW-Authenticate": "Custom Token"}
