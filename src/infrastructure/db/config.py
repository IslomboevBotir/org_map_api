from functools import cache
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from src.infrastructure.settings import get_settings

settings = get_settings()


@cache
def async_general_engine() -> AsyncEngine:
    return create_async_engine(
        settings.ASYNC_DB_URL,
        pool_size=settings.ASYNC_DB_POOL_SIZE,
        echo_pool=True
    )


@cache
def async_general_session_maker(
        general_engine: AsyncEngine = Depends(async_general_engine)
) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=general_engine,
        autocommit=False,
        autoflush=False
    )


async def async_general_session(
        general_session_maker: async_sessionmaker[AsyncSession] = Depends(async_general_session_maker)
) -> AsyncGenerator[AsyncSession, None]:
    async with general_session_maker() as session:
        yield session


@cache
def sync_general_engine() -> Engine:
    return create_engine(
        settings.SYNC_DB_URL,
        future=True
    )


@cache
def sync_general_session_maker() -> sessionmaker:
    return sessionmaker(
        bind=sync_general_engine(),
        autocommit=False,
        autoflush=False
    )


def sync_general_session() -> Session:
    session_factory = sync_general_session_maker()
    return session_factory()
