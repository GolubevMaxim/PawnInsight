from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database.user_orm import UserORM
from backend.users.user_sсheme import UserScheme


async def get_all_users(db: AsyncSession):
    s = select(UserORM)
    return (await db.scalars(s)).all()


async def get_user_by_id(user_id, db: AsyncSession):
    s = select(UserORM).where(UserORM.id == user_id)
    return (await db.scalars(s)).all()


async def add_user(user, db: AsyncSession):
    new_user = UserORM(**user.model_dump())
    db.add(new_user)
    await db.commit()


async def update_user(user: UserScheme, db: AsyncSession):
    user = user.model_dump()
    s = select(UserORM).where(UserORM.id == user["id"])
    db_user = (await db.scalars(s)).first()
    for key, value in user.items():
        setattr(db_user, key, value)
    await db.commit()


async def delete_user(user_id: int, db: AsyncSession):
    s = select(UserORM).where(UserORM.id == user_id)
    db_user = (await db.scalars(s)).first()
    await db.delete(db_user)
    await db.commit()
