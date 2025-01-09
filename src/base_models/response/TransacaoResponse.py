from pydantic import BaseModel


class TransacaoResponse(BaseModel):
    id: int
    tipo: str
    valor: float