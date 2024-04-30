from flask import Blueprint, jsonify, make_response, request
from controllers.censoControl import CensoControl
from controllers.utils.errors import Erros
from flask_expects_json import expects_json

api_censo = Blueprint('api_censo', __name__)

# API para Persona
censoC = CensoControl()

# Validadores
schema = {
    "type": "object",
    'properties': {
        "fecha_in": {"type": "string"},
        "fecha_fin": {"type": "string"},
        "motivo": {"type": "string"},
        "estado": {"type": "boolean"},
    },
    'required': ["fecha_in", "fecha_fin", "motivo", "estado"]
}
censo_persona_schema = {
    "type": "object",
    'properties': {
        "lat": {"type": "number"},
        "long": {"type": "number"},
        "motivo": {"type": "string"},
    },
    'required': ["lat", "long", "motivo"]
}

# API para listar censo
@api_censo.route("/censo")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize() for i in censoC.listar()]}),
        200
    )

# API para guardar un censo
@api_censo.route("/censo/guardar", methods=["POST"])
@expects_json(schema)
def guardar():
    data = request.json
    m = censoC.guardar(data)
    if (m == 0):
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": []}),
            200
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": []}),
        200
    )

# API para listar un censo por external_id
@api_censo.route("/censo/<external_id>", methods=["GET"])
def obtener(external_id):
    censo = censoC.obtener_por_external_id(external_id)
    if censo:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": censo.serialize()}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": "Censo no encontrado", "code": 404}),
            404
        )
    
# Api para modificar un censo por external_id
@api_censo.route("/censo/modificar/<external_id>", methods=["POST"])
@expects_json(schema)
def modificar(external_id):
    data = request.json
    censo = censoC.modificar(external_id, data)
    if censo:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": censo.serialize()}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": "Censo no encontrado", "code": 404}),
            404
        )
    
# Api para activar un censo por external_id
@api_censo.route("/censo/activar/<external_id>", methods=["GET"])
def activar(external_id):
    censo = censoC.activar_censo(external_id)
    if censo:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": censo.serialize()}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": "Censo no encontrado", "code": 404}),
            404
        )

# Api para desactivar un censo por external_id
@api_censo.route("/censo/desactivar/<external_id>", methods=["GET"])
def desactivar(external_id):
    censo = censoC.desactivar_censo(external_id)
    if censo:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": censo.serialize()}),
            200
        )
    else:
        return make_response(
            jsonify({"msg": "Censo no encontrado", "code": 404}),
            404
        )

@api_censo.route("/guardar/censo/persona", methods=["POST"])
@expects_json(censo_persona_schema)
def guardar_datos():
    data = request.json
    id_censo_persona = censoC.guardar_datos_censo(data)
    if id_censo_persona == -4:
        return make_response(
            jsonify({"msg": "Motivo no encontrado", "code": 404}),
            404
        )
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": id_censo_persona}),
        200
    )
