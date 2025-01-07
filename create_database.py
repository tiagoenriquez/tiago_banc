import sys
import os
from src.databases.connection import get_connection

sys.path.append(os.path.abspath("."))

async def run():
    from src.databases.create_tables import create
    await create()

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())