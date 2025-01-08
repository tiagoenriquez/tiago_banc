from fastapi import APIRouter, Depends, status, HTTPException

from src.auth import Auth
from src.base_models.request.ContaRequest import ContaRequest
from src.services import ContaService


router = APIRouter(prefix="/contas", dependencies=[Depends(Auth().decode)])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def inserir(conta: ContaRequest):
    await ContaService.inserir(conta)
    return {"message": "Conta cadastrada com sucesso"}