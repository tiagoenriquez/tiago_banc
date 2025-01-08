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
        await self.__manipulate(f"delete from {self.table()} where id = {self.id}")
    
    @classmethod
    async def find_all(cls):
        return await cls.__find_many(f"select * from {cls.class_table()}")
    
    @classmethod
    async def find_all_sorted(cls, key: str, towards = "desc"):
        return await cls.__find_many(f"select * from {cls.class_table()} order by {towards} {key}")
    
    @classmethod
    async def find_by_id(cls, id: int):
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(f"select * from {cls.class_table()} where id = {id}")
            result = await cursor.fetchone()
            if not result:
                return None
            return cls.__convert_select(result, cursor)
    
    @classmethod
    async def find_by_key(cls, key: str, value: any):
        return await cls.__find_many(f"select * from {cls.class_table()} where {key} = ?", [value])
    
    @classmethod
    async def find_by_key_sorted(cls, key: str, value: any, sorted_key: str, towards = "desc"):
        return await cls.__find_many(
            f"select * from {cls.class_table()} " +
            f"where {key} = ? order by {towards} {sorted_key}",
            [value]
        )
    
    @classmethod
    async def find_paginated(cls, limit: int, offset: int):
        return await cls.__find_many(f"select * from {cls.class_table()} limit {limit} offset {offset}")
    
    @classmethod
    async def find_paginated_by_key(cls, key: str, value: str, limit: int, offset: int):
        return await cls.__find_many(
            f"select * from {cls.class_table()} " +
            f"where {key} = ? limit {limit} offset {offset}",
            [value]
        )
    
    async def insert(self) -> None:
        await self.__manipulate(
            f"insert into {self.table()} ({', '.join(self.keys()[1:])}) values ({'?, ' * (len(self.values()) - 2)}?)",
            self.values()[1: ]
        )
    
    async def update(self) -> None:
        await self.__manipulate(
            f"update {self.table()} set {' = ?, '.join(self.keys()[1:])} = ? where id = {self.id}",
            self.values()[1:]
        )
    
    @classmethod
    def __convert_select(cls, result, cursor: Cursor):
        fields = []
        for description in cursor.description:
            fields.append(description[0])
        return cls(**dict(zip(fields, result)))
    
    @classmethod
    async def __find_many(cls, query: str, data = []):
        async with await get_connection() as connection:
            cursor = await connection.cursor()
            await cursor.execute(query, data)
            result = await cursor.fetchall()
            if not result:
                return None
            instances = []
            for row in result:
                instances.append(cls.__convert_select(row, cursor))
            return instances 

    async def __manipulate(self, query: str, data = []) -> None:
        async with await get_connection() as connection:
            await connection.execute(query, data)
            await connection.commit()