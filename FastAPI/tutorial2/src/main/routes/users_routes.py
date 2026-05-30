from fastapi import APIRouter
from fastapi.responses import JSONResponse

from FAstAPi.tutorial2.src.main.validators.user_register_validator import UserRegisterValidator

users_routes = APIRouter(tags=["Usuários"])

@users_routes.post("/users")
async def create_user(body: UserRegisterValidator):
    dict_body = dict(body)
    return JSONResponse(
        status_code=201,
        content={
            "message":"Usuário criado com susseso!",
            "att": dict_body
        }
    )