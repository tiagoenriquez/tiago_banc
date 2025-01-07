import sys
import os

from fastapi import FastAPI

sys.path.append(os.path.abspath("."))


from src.controllers import UsuarioController


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(UsuarioController.router)