from os import environ
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import BaseModel
import jwt

from src.models.Usuario import Usuario


JWT_ALGORITHM = "HS256"

class Payload(BaseModel):
    id: int
    cpf: str
    perfil: str

class Auth:
    def encode(self, usuario: Usuario) -> str:
        load_dotenv()
        return jwt.encode(
            Payload(id=usuario.id, cpf=usuario.cpf, perfil=usuario.perfil).__dict__,
            environ["JWT_TOKEN"],
            algorithm=JWT_ALGORITHM
        )
    
    async def decode(self, token: Annotated[Payload, Depends(HTTPBearer())]):
        try:
            load_dotenv()
            jwt.decode(token.credentials, environ["JWT_TOKEN"], algorithms=[JWT_ALGORITHM])
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido")
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirado")
        except Exception as exception:
            raise Exception("Falha na autenticação")