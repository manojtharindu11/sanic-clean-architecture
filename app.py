from sanic import Sanic

from api.routes.user_routes import user_bp


def create_app():

    app = Sanic("UserService")

    app.blueprint(user_bp)

    return app
