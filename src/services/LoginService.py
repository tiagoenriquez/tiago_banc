from bcrypt import checkpw

from src.auth import Auth
from src.base_models.request.LoginRequest import LoginRequest
from src.base_models.response.JWTTokenResponse import JWTTokenResponse
from src.models.Usuario import Usuario


JWT_ALGORITHM = "HS256"

async def logar(login: LoginRequest) -> JWTTokenResponse:
    result = await Usuario.find_by_key("cpf", login.cpf)
    if not result:
        raise Exception("Credenciais inválidas")
    usuario = result[0]
    if not checkpw(login.senha.encode("utf-8"), usuario.senha):
        raise Exception("Credencias inválidas")
    return JWTTokenResponse(token=Auth().encode(usuario))