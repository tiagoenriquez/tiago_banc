from src.models.Model import Model


class Conta(Model):
    def __init__(self, numero: int, saldo: float, usuario_id: int, id: int | None = None) -> None:
        self.id = id
        self.numero = numero
        self.saldo = saldo