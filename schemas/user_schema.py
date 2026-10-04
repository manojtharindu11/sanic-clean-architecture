from pydantic import BaseModel, EmailStr, Field


class CreateUserRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=18)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
