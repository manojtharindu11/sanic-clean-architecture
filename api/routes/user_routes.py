from sanic import BadRequest, Blueprint
from sanic.response import json
from controllers.user_controller import get_user_hello, create_user
from schemas.user_schema import CreateUserRequest

user_bp = Blueprint("users", url_prefix="/api/v1/users")


@user_bp.get("/hello")
async def hello_user(request):
    response = await get_user_hello()
    return json(response)


@user_bp.post("/")
async def create_user_route(request):
    try:
        data = CreateUserRequest.model_validate(request.json)
    except ValueError as exc:
        raise BadRequest(str(exc))

    user = await create_user(data)
    return json(user.model_dump())
