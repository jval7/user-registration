from pydantic import BaseModel, EmailStr, Field


class CreateUserSchema(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr
    city: str = Field(..., max_length=100)


class UserSchema(CreateUserSchema):
    id: int

    class Config:
        orm_mode = True
