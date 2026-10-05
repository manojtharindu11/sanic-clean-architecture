from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: list[User] = []
        self._next_id = 1

    async def create(self, user: User) -> User:
        user.id = self._next_id
        self._next_id += 1
        self._users.append(user)
        return user

    async def get_by_id(self, user_id: int) -> User | None:
        return next((user for user in self._users if user.id == user_id), None)
