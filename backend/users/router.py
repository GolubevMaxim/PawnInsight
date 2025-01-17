from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.users.user_sсheme import UserScheme, UserAddScheme
from backend.users import controller
from backend.database.database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", summary="get all users")
async def get_users(db: AsyncSession = Depends(get_db)):
    return await controller.get_all_users(db)


@router.get("/{user_id}", summary="get user")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await controller.get_user_by_id(user_id, db)


@router.post("/", summary="create user")
async def create_user(user: UserAddScheme, db: AsyncSession = Depends(get_db)):
    try:
        print(user)
        await controller.add_user(user, db)
    except Exception as e:
        return {"error": str(e)}
    return {"message": "User created"}


@router.put("/{user_id}", summary="update user")
async def update_user(user: UserScheme, db: AsyncSession = Depends(get_db)):
    try:
        print(user)
        await controller.update_user(user, db)
    except Exception as e:
        return {"error": str(e)}
    return {"message": "User updated"}


@router.delete("/{user_id}", summary="delete user")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        print(user_id)
        await controller.delete_user(user_id, db)
    except Exception as e:
        return {"error": str(e)}
    return {"message": "User deleted"}