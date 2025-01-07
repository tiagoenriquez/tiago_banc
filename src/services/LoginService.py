from os import environ

from bcrypt import checkpw, hashpw
from dotenv import load_dotenv
import jwt

from src.base_models.request.LoginRequest import LoginRequest
from src.base_models.response.JWTTokenResponse import JWTTokenResponse
from src.models.Usuario import Usuario


JWT_ALGORITHM = "HS256"

async def logar(login: LoginRequest) -> JWTTokenResponse:
    result = await Usuario.find("cpf", login.cpf)
    if not result or checkpw(login.senha.encode("utf-8"), usuario.senha):
        raise Exception("Credencias inválidas")
    usuario = result[0]
    load_dotenv()
    return JWTTokenResponse(token=jwt.encode(
        {
            "cpf": usuario.cpf,
            "perfil": usuario.perfil
        },
        environ["JWT_TOKEN"],
        algorithm=JWT_ALGORITHM)
    )