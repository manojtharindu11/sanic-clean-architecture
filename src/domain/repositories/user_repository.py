from abc import ABC, abstractmethod

from domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User | None:
        raise NotImplementedError
