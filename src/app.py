from sanic import Sanic

from application.users.create_user import CreateUser
from infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)
from presentation.http.user_routes import create_user_blueprint


def create_app() -> Sanic:
    app = Sanic("UserService")

    user_repository = InMemoryUserRepository()
    create_user = CreateUser(user_repository)
    app.blueprint(create_user_blueprint(create_user))

    return app
