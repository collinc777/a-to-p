from typing import AsyncGenerator, AsyncIterator
from alembic import op
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from api.settings import get_settings

database_url = get_settings().database_url
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set")
async_engine = create_async_engine(database_url)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )  # type: ignore
    async with async_session() as session:
        yield session


@asynccontextmanager
async def get_session_context() -> AsyncIterator[AsyncSession]:
    async_session = async_sessionmaker(
        bind=async_engine,
        expire_on_commit=False,
    )
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.close()


def get_session_for_migrations(bind: Connection):
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=bind)
    session = Session()
    return session
