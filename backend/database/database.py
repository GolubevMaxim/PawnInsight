from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

engine = create_async_engine("sqlite+aiosqlite:///pawn_insight.sqlite3")
new_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncSession:
    db = new_session()
    try:
        yield db
    finally:
        await db.close()


class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)


async def create_tables():
    async with engine.connect() as conn:
        print(Base.metadata.tables)
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

