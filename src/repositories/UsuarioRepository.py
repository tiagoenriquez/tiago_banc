# from src.databases.connection import connection

# from src.models.Usuario import Usuario


# __table = "usuarios"

# async def has() -> bool:
#     async with connection:
#         cursor = await connection.cursor()
#         await cursor.execute("select id from usuarios limit 1")
#         result = await cursor.fetchone()
#         if not result:
#             return False
#         return True


# async def insert(usuario: Usuario) -> None:
#     async with connection:
#         await connection.execute(f"insert into {__table} ({', '.join(usuario.fields())}) values ()")