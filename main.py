from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from src.dependencies import check_Oauth2
from src.models.ErrorModel import AuthorizedException
from src.routers import Bank

app = FastAPI(dependencies=[Depends(check_Oauth2)])

app.include_router(Bank.router)

@app.exception_handler(AuthorizedException)
async def authorize_exception_handler(request: Request, exc: AuthorizedException):
    return JSONResponse(content=exc.content, status_code=exc.status_code)


@app.get('/')
def root():
    return "Ckao` em"