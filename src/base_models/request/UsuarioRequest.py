from pydantic import BaseModel


class UsuarioRequest(BaseModel):
    nome: str
    cpf: str
    senha: str
    confirmacao: str