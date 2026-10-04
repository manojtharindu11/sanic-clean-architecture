from sanic import Blueprint
from sanic.response import json

user_bp = Blueprint("users", url_prefix="/api/v1/users")


@user_bp.get("/hello")
async def hello_user(request):
    return json({"message": "Hello User"})
