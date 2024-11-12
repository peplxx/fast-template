from sqlalchemy import select

from app.db.connection import get_session


async def database_healthcheck() -> bool:
    """ Checks if the database is accessible. """
    try:
        async for session in get_session():
            await session.execute(select(1))
        return True
    except Exception as e:
        print(e)
        return False