import sys
import os

from src.databases.connection import get_connection
from src.databases.definitions import ContaDefinition, TransacaoDefinition, UsuarioDefinition


sys.path.append(os.path.abspath(os.path.dirname(__file__)))


async def create():
    async with await get_connection() as connection:
        cursor = await connection.cursor()
        await cursor.execute(UsuarioDefinition.definition)
        await cursor.execute(ContaDefinition.definition)
        await cursor.execute(TransacaoDefinition.definition)
        await connection.commit()