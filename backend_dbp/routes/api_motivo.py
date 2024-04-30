from flask import Blueprint, jsonify, make_response, request
from controllers.motivoControl import MotivoControl
from controllers.utils.errors import Erros
from flask_expects_json import expects_json

api_motivo = Blueprint('api_motivo', __name__)

# API para Motivo
motivoC = MotivoControl()
# Validadores
schema = {
    "type": "object",
    'properties': {
        "nombre": {"type": "string"},
    },
    'required': ["nombre"]
}

@api_motivo.route("/motivo")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize() for i in motivoC.listar()]}),
        200
    )

@api_motivo.route("/motivo/activos")
def listar_activos():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize() for i in motivoC.listar_activos()]}),
        200
    )

# Api para guardar un motivo
@api_motivo.route("/motivo/save/str", methods=["POST"])
@expects_json(schema)
def save_str():
    data = request.json
    m = motivoC.save_str(request.json['nombre'])
    if (m == 0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": []}),
            200
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": []}),
        200
    )

# Api para activar un motivo
@api_motivo.route("/motivo/activar/<external_id>", methods=["GET"])
def activar(external_id):
    m = motivoC.activar(external_id)
    if (m == 0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": []}),
            200
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": []}),
        200
    )

# Api para desactivar un motivo
@api_motivo.route("/motivo/desactivar/<external_id>", methods=["GET"])
def desactivar(external_id):
    m = motivoC.desactivar(external_id)
    if (m == 0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": []}),
            200
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": []}),
        200
    )