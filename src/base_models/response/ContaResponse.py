from pydantic import BaseModel

from base_models.response.TransacaoResponse import TransacaoResponse


class ContaResponse(BaseModel):
    id: int
    numero: int
    saldo: float
    transacoes: list[TransacaoResponse]