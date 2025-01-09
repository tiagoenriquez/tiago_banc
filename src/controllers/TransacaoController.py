from fastapi import APIRouter, Depends, HTTPException, status

from src.auth import Auth
from src.base_models.request.TransacaoRequest import TransacaoRequest
from src.services import TransacaoService


router = APIRouter(prefix="/transacoes", dependencies=[Depends(Auth().decode)])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def inserir(transacao: TransacaoRequest):
    try:
        await TransacaoService.inserir(transacao)
        return {"message": "Transação realizada com sucesso"}
    except Exception as exception:
        raise HTTPException(status.HTTP_409_CONFLICT, exception.args[0])