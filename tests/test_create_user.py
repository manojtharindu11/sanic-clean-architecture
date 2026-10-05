import asyncio

from application.users.create_user import (
    CreateUser,
    CreateUserCommand,
)
from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)


def test_create_user_uses_injected_repository():
    use_case = CreateUser(InMemoryUserRepository())

    user = asyncio.run(
        use_case.execute(
            CreateUserCommand(
                name="Ada Lovelace",
                email="ada@example.com",
                age=36,
            )
        )
    )

    assert user.id == 1
    assert user.name == "Ada Lovelace"
    assert user.email == "ada@example.com"
