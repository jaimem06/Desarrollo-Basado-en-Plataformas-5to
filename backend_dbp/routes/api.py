from flask import Blueprint, jsonify, make_response, request
# Importacion de los modelos de tablas de la base de datos
from models.rol import Rol
from models.practicando import Practicando

api = Blueprint('api', __name__)

@api.route("/")
def home ():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )

@api.route("/suma/<a>/<b>")
def suma (a, b):
    c= float(a) + float(b)
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": {"suma": c}}),
        200     
    )

@api.route("/sumar", methods=["POST"])
def suma_post():
    data = request.json
    a = float(data["a"])
    b = float(data["b"])
    c = a + b
    return make_response(
        jsonify({"msg": "OK", "code": 200, "data": {"suma": c}}),
        200
    )