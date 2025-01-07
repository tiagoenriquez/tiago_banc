from bcrypt import hashpw, gensalt

from src.base_models.request.UsuarioRequest import UsuarioRequest
from src.base_models.response.UsuarioResponse import UsuarioResponse
from src.models.Usuario import Usuario


async def inserir(us_req: UsuarioRequest):
    qtd = await Usuario.count()
    perfil = ""
    if qtd > 0:
        perfil = "normal"
    else:
        perfil = "administrador"
    __validar(us_req)
    usuario = Usuario(us_req.nome, us_req.cpf, perfil, hashpw(us_req.senha.encode("utf-8"), gensalt()))
    await usuario.insert()

async def listar_paginado(limit: int, skip = 0) -> UsuarioResponse:
    pass

def __validar(us_req: UsuarioRequest):
    if not us_req.nome:
        raise Exception("O nome não foi informado")
    if not us_req.cpf:
        raise Exception("O CPF não foi informado")
    if us_req.confirmacao != us_req.senha:
        raise Exception("Senhas não conferem")