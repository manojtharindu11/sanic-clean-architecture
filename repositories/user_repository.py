from entities.user import User


class UserRepository:

    def __init__(self):
        self._users: list[User] = []
        self._next_id = 1

    async def create(self, user: User) -> User:
        user.id = self._next_id
        self._next_id += 1

        self._users.append(user)

        return user

    async def get_by_id(self, user_id: int) -> User | None:
        for user in self._users:
            if user.id == user_id:
                return user

        return None
