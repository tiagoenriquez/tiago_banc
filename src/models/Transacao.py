from src.models.Model import Model


class Transacao(Model):
    def __init__(self, valor: float, tipo: str, conta_id: int, id: int | None = None) -> None:
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.conta_id = conta_id