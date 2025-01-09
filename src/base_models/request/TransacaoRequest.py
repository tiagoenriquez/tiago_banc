from pydantic import BaseModel


class TransacaoRequest(BaseModel):
    valor: float
    tipo: str
    conta_id: int