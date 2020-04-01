from .cat import api as cat_ns
from .dog import api as dog_ns

from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="FLASK RESTX API", version="1.0", description="FLASK RESTX API "
)


api.add_namespace(cat_ns, path="/cat")
api.add_namespace(dog_ns, path="/dog")
