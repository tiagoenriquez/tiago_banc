from fastapi import APIRouter, Depends, status

from src.auth import Auth
from src.base_models.response.ContaResponse import ContaResponse
from base_models.response.TransacaoResponse import TransacaoResponse
from src.base_models.request.ContaRequest import ContaRequest
from src.services import ContaService


router = APIRouter(prefix="/contas", dependencies=[Depends(Auth().decode)])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def inserir(conta: ContaRequest):
    await ContaService.inserir(conta)
    return {"message": "Conta cadastrada com sucesso"}

@router.get("/{id}", response_model=ContaResponse)
async def procurar(id):
    conta = await ContaService.procurar(id)
    transacoes = await conta.transacoes()
    transacoes_res: list[TransacaoResponse] = []
    if transacoes:
        for transacao in transacoes:
            transacoes_res.append(TransacaoResponse(id=transacao.id, tipo=transacao.tipo, valor=transacao.valor))
    return ContaResponse(id=conta.id, numero=conta.numero, saldo=conta.saldo, transacoes=transacoes_res)