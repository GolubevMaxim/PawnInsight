from pydantic import BaseModel, Field, EmailStr


class UserAddScheme(BaseModel):
    user_name: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=50)
    password: str = Field(min_length=1, max_length=50)


class UserScheme(UserAddScheme):
    id: int = Field(ge=1)
