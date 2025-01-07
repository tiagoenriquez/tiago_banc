from bcrypt import hashpw, gensalt

from src.base_models.request.UsuarioRequest import UsuarioRequest
from src.models.Usuario import Usuario


async def inserir_primeiro(us_req: UsuarioRequest):
    qtd = await Usuario.count()
    if qtd > 0:
        raise Exception("Este não é o primeiro salvo no sistema.")
    __validar(us_req)
    usuario = Usuario(us_req.nome, us_req.cpf, "administrador", hashpw(us_req.senha.encode("utf-8"), gensalt()))
    await usuario.insert()

def __validar(us_req: UsuarioRequest):
    if not us_req.nome:
        raise Exception("O nome não foi informado")
    if not us_req.cpf:
        raise Exception("O CPF não foi informado")
    if us_req.confirmacao != us_req.senha:
        raise Exception("Senhas não conferem")