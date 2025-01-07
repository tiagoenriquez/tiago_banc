from pydantic import BaseModel


class JWTTokenResponse(BaseModel):
    token: str