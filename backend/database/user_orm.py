from sqlalchemy.orm import Mapped

from .database import Base


class UserORM(Base):
    user_name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
