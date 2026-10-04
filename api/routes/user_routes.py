from sanic import BadRequest, Blueprint
from sanic.response import json
from controllers.user_controller import UserController
from repositories.user_repository import UserRepository
from schemas.user_schema import CreateUserRequest

user_bp = Blueprint("users", url_prefix="/api/v1/users")

repository = UserRepository()
controller = UserController(repository)


@user_bp.get("/hello")
async def hello_user(request):
    response = {"message": "Hello User"}
    return json(response)


@user_bp.post("/")
async def create_user_route(request):
    try:
        data = CreateUserRequest.model_validate(request.json)
    except ValueError as exc:
        raise BadRequest(str(exc))

    user = await controller.create_user(data)
    return json(user.model_dump())
