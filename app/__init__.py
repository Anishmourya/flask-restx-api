from flask import Flask
from flask import make_response
from app.apis import blueprint as api


# flask app factory to create app


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return make_response(({"success": True}), 200)

    app.register_blueprint(api, url_prefix="/v1")
    return app
