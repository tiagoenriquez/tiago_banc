import sys
import os

from fastapi import FastAPI

sys.path.append(os.path.abspath("."))


from src.controllers import ContaController
from src.controllers import LoginController, TransacaoController, UsuarioController


tags_metadata = [
    {"name": "usuário", "description": "Manipulação de pesquisa relacionada a usuários"},
    {"name": "login", "description": "Login de usuários"},
    {"name": "conta", "description": "Manipulação de pesquisa relacionada a contas bancárias"},
    {"name": "transação", "description": "Manipulação de pesquisa relacionada a transações"}
]

app = FastAPI(
    title="Web Service Bancária de Tiago Tachy",
    version="1.0.0",
    summary="Web service para cadastro de saques e depósitos em contas bancárias",
    description="""
Métodos disponíveis:
## Usuário:
* **Cadastro**.
## Login:
* **Login**.
## Conta:
* **Cadastro**.
* **Dados de uma conta com transações relacionadas**.
## Transação:
* **Cadastro**.
""",
    openapi_tags=tags_metadata,
    redoc_url=None
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(UsuarioController.router, tags=["usuário"])
app.include_router(LoginController.router, tags=["login"])
app.include_router(ContaController.router, tags=["conta"])
app.include_router(TransacaoController.router, tags=["transação"])