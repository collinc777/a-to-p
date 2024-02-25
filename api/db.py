from typing import AsyncGenerator, AsyncIterator
from fastapi.concurrency import asynccontextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlmodel import create_engine
from api.settings import get_settings

async_engine = AsyncEngine(create_engine(get_settings().database_url))  # type: ignore


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


@asynccontextmanager
async def get_session_context() -> AsyncIterator[AsyncSession]:
    async_session = sessionmaker(
        bind=async_engine,  # type: ignore
        class_=AsyncSession,
        expire_on_commit=False,
    )
    session: AsyncSession = async_session()  # type: ignore
    try:
        yield session
    finally:
        await session.close()
