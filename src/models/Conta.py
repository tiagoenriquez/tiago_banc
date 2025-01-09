from src.models.Model import Model
from src.models.Transacao import Transacao


class Conta(Model):
    def __init__(self, numero: int, saldo: float, usuario_id: int, id: int | None = None) -> None:
        self.id = id
        self.numero = numero
        self.saldo = saldo
        self.usuario_id = usuario_id
    
    async def transacoes(self) -> list[Transacao]:
        return await Transacao.find_by_key("conta_id", self.id)