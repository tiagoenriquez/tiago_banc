from fastapi import APIRouter, status, HTTPException

from src.base_models.request.UsuarioRequest import UsuarioRequest
from src.services import UsuarioService


router = APIRouter(prefix="/usuarios")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def inserir(usuario: UsuarioRequest):
    try:
        await UsuarioService.inserir(usuario)
        return {"message": "Usuário cadastrado com sucesso"}
    except Exception as exception:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, exception.args[0])