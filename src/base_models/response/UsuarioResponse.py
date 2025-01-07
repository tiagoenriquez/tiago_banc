from pydantic import BaseModel


class UsuarioResponse(BaseModel):
    nome: str
    cpf: str
    perfil: str