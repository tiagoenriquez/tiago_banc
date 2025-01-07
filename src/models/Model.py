from sqlite3 import Cursor

from src.databases.connection import get_connection


class Model:
    @classmethod
    def class_table(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def keys(self) -> list:
        keys = list(self.__dict__.keys())
        return keys[0: len(keys)]    

    def table(self) -> str:
        return f"{self.__class__.__name__.lower()}s"
    
    def values(self):
        values = list(self.__dict__.values())
        return values[0: len(values)]
    
    @classmethod
    async def count(cls) -> int:
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(f"select count(*) from {cls.class_table()}")
            result = await cursor.fetchone()
            return result[0]
    
    async def delete(self) -> None:
        async with await get_connection() as connection:
            await connection.execute(f"delete from {self.table()} where id = {self.id}")
            await connection.commit()
    
    @classmethod
    async def find(cls, key: str, value: any):
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(f"select * from {cls.class_table()} where {key} = ?", [value])
            result = await cursor.fetchall()
            if not result:
                return None
            instances = []
            for row in result:
                instances.append(cls.__convert_select(row, cursor))
            return instances
    
    @classmethod
    async def find_all(cls):
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(f"select * from {cls.class_table()}")
            result = await cursor.fetchall()
            if not result:
                return None
            instances = []
            for row in result:
                instances.append(cls.__convert_select(row, cursor))
            return instances
    
    @classmethod
    async def find_by_id(cls, id: int):
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(f"select * from {cls.class_table()} where id = {id}")
            result = await cursor.fetchone()
            if not result:
                return None
            return cls.__convert_select(result, cursor)
    
    async def insert(self) -> None:
        async with await get_connection() as connection:
            await connection.execute(
                f"insert into {self.table()} ({', '.join(self.keys()[1:])}) " +
                f"values ({'?, ' * (len(self.values()) - 2)}?)",
                self.values()[1: ]
            )
            await connection.commit()
    
    async def update(self) -> None:
        async with await get_connection() as connection:
            await connection.execute(
                f"update {self.table()} set {' = ?, '.join(self.keys()[1:])} = ? where id = {self.id}",
                self.values()[1:]
            )
            await connection.commit()
    
    @classmethod
    def __convert_select(cls, result, cursor: Cursor):
        fields = []
        for description in cursor.description:
            fields.append(description[0])
        return cls(**dict(zip(fields, result)))