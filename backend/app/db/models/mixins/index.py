from uuid import uuid4, UUID

import sqlalchemy as sa
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped

class UUIDMixin:
    __abstract__ = True
    id: Mapped[UUID] = sa.Column(sa.UUID, nullable=False, primary_key=True, default=uuid4)

    @classmethod
    async def find_by_id(cls, session: AsyncSession, entity_id: UUID):
        return await session.scalar(select(cls).where(cls.id == entity_id))

class IDMixin:
    __abstract__ = True
    id: Mapped[int] = sa.Column(sa.Integer, nullable=False, primary_key=True, autoincrement=True)

    @classmethod
    async def find_by_id(cls, session: AsyncSession, entity_id: int):
        return await session.scalar(select(cls).where(cls.id == entity_id))
    
__all__ = ["UUIDMixin", "IDMixin"]