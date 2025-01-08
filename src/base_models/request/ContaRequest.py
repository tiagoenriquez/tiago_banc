from pydantic import BaseModel


class ContaRequest(BaseModel):
    numero: int
    usuario_id: int