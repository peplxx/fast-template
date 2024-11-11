__all__ = ["get_session", "database_healthcheck"]

from threading import Lock

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

from app.config import get_settings

settings = get_settings()


class SessionManager:
    _instance = None
    _lock = Lock()
    session_maker: sessionmaker = None
    engine: AsyncEngine

    def __init__(self) -> None:
        self.refresh()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(SessionManager, cls).__new__(cls)
                cls._instance.refresh()
            return cls._instance

    def get_session_maker(self) -> sessionmaker:
        if not self.session_maker:
            self.session_maker = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)
        return self.session_maker

    def default_engine(self):
        self.engine = create_async_engine(
            get_settings().database_uri,
            echo=True,
            future=True,
            connect_args=settings.db_context
        )

    def refresh(self) -> None:
        self.default_engine()


async def get_session() -> AsyncSession:
    session_maker = SessionManager().get_session_maker()
    async with session_maker() as session:
        yield session


async def database_healthcheck() -> bool:
    """ Checks if the database is accessible. """
    try:
        async for session in get_session():
            await session.execute(select(1))
        return True
    except Exception as e:
        print(e)
        return False
