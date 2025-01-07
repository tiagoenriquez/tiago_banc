import sys
import os

from fastapi import FastAPI

sys.path.append(os.path.abspath("."))


from src.controllers import LoginController, UsuarioController


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(UsuarioController.router)
app.include_router(LoginController.router)