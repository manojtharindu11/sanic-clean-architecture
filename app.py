from sanic import Sanic
from sanic.response import json

app = Sanic("UserService")


@app.get("/hello")
async def hello(request):
    return json({"message": "Hello Sanic"})
