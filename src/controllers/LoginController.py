from fastapi import APIRouter, status, HTTPException

from src.base_models.request.LoginRequest import LoginRequest
from src.base_models.response.JWTTokenResponse import JWTTokenResponse
from src.services import LoginService


router = APIRouter(prefix="/login")

@router.post("/", response_model=JWTTokenResponse)
async def logar(login: LoginRequest) -> JWTTokenResponse:
    try:
        return await LoginService.logar(login)
    except Exception as exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=exception.args[0])