from src.base_models.request.ContaRequest import ContaRequest
from src.models.Conta import Conta


async def inserir(conta_request: ContaRequest) -> None:
    conta = Conta(conta_request.numero, 0.0, conta_request.usuario_id)
    await conta.insert()