from entities.user import User
from repositories.user_repository import UserRepository
from schemas.user_schema import CreateUserRequest, UserResponse


class UserController:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(
        self,
        data: CreateUserRequest,
    ) -> UserResponse:

        user = User(
            id=0,
            name=data.name,
            email=str(data.email),
            age=data.age,
        )

        saved_user = await self.repository.create(user)

        return UserResponse(
            id=saved_user.id,
            name=saved_user.name,
            email=saved_user.email,
            age=saved_user.age,
        )
