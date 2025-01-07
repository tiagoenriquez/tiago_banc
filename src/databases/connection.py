import aiosqlite


async def get_connection():
    return aiosqlite.connect("db.sqlite3")