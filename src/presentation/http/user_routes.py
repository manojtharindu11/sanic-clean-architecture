from sanic import BadRequest, Blueprint, Request
from sanic.response import json

from application.users.create_user import (
    CreateUser,
    CreateUserCommand,
)
from presentation.schemas.user_schema import (
    CreateUserRequest,
    UserResponse,
)


def create_user_blueprint(create_user: CreateUser) -> Blueprint:
    user_bp = Blueprint("users", url_prefix="/api/v1/users")

    @user_bp.get("/hello")
    async def hello_user(_request: Request):
        del _request
        return json({"message": "Hello User"})

    @user_bp.post("/")
    async def create_user_route(request: Request):
        try:
            request_data = CreateUserRequest.model_validate(request.json)
        except ValueError as exc:
            raise BadRequest(str(exc)) from exc

        user = await create_user.execute(
            CreateUserCommand(
                name=request_data.name,
                email=str(request_data.email),
                age=request_data.age,
            )
        )
        response = UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            age=user.age,
        )
        return json(response.model_dump())

    return user_bp
