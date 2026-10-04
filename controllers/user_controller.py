from schemas.user_schema import CreateUserRequest, UserResponse


async def get_user_hello():
    return {"message": "Hello User"}

async def create_user(data: CreateUserRequest) -> UserResponse:
    user = UserResponse(
        id = 1,
        name = data.name,
        email = data.email,
        age = data.age
    )

    return user
