from src.base_models.request.TransacaoRequest import TransacaoRequest
from src.models.Conta import Conta
from src.models.Transacao import Transacao


tipos = ["depósito", "saque"]

async def inserir(trans_req: TransacaoRequest) -> None:
    tipo = trans_req.tipo
    if tipo not in tipos:
        raise Exception("Tipo inválido")
    valor = trans_req.valor
    conta = await Conta.find_by_id(trans_req.conta_id)
    saldo = conta.saldo
    if valor <= 0:
        raise Exception("Valor inválido")
    if valor > saldo and tipo == "saque":
        raise Exception("Saldo insuficiente")
    transacao = Transacao(valor, tipo, conta.id)
    await transacao.insert()
    conta.saldo = saldo + valor if tipo == "depósito" else saldo - valor
    await conta.update()