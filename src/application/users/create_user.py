from dataclasses import dataclass

from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class CreateUserCommand:
    name: str
    email: str
    age: int


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, command: CreateUserCommand) -> User:
        user = User(
            id=0,
            name=command.name,
            email=command.email,
            age=command.age,
        )
        return await self._user_repository.create(user)
