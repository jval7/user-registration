from pydantic import BaseModel, EmailStr, Field


class CreateUserSchema(BaseModel):
    name: str = Field(..., max_length=10)
    email: EmailStr
    city: str = Field(..., max_length=20)


class UserSchema(CreateUserSchema):
    id: int

    class Config:
        orm_mode = True
