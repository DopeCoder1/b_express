from src.database import async_session_maker
from sqlalchemy import select,insert
from typing import Any

class BaseDao:
    class_name = None
    
    @classmethod
    async def find_by_id(cls, id:int):
        async with async_session_maker() as session:
            query = select(cls.class_name).filter_by(id=id)
            data = await session.execute(query)
            resp = data.scalar_one_or_none()
            return resp
    
    @classmethod
    async def find_one_or_none(cls, filter):
        async with async_session_maker() as session:
            query = select(cls.class_name).filter_by(**filter)
            data = await session.execute(query)
            resp = data.scalar_one_or_none()
            return resp
        
    @classmethod
    async def find_all(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.class_name).filter_by(**filter)
            data = await session.execute(query)
            resp = data.scalars().all()
            return resp
            
    @classmethod
    async def add(cls, data: Any):
        async with async_session_maker() as session:
            query = insert(cls.class_name).values(**data)
            await session.execute(query)
            await session.commit()