from flask import Blueprint, jsonify, make_response, request
from controllers.personaControl import PersonaControl
from controllers.utils.errors import Erros
from flask_expects_json import expects_json

api_persona = Blueprint('api_persona', __name__)

# API para Persona
personaC = PersonaControl()

schema = {
    "type": "object",
    'properties': {
        "nombre": {"type": "string"},
        "apellido": {"type": "string"},
        "fecha": {"type": "string"},
        "estado": {"type": "boolean"},
    },
    'required': ["nombre", "apellido", "fecha", "estado"]
}

@api_persona.route("/persona")
def listar():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": [i.serialize() for i in personaC.listar()]}),
        200
    )

@api_persona.route("/persona.post", methods=['POST'])
def crear():
    data = request.get_json()
    result = personaC.crear(data)
    if result:
        return make_response(jsonify({"msg": "OK", "code": 201, "datos": result.serialize()}), 201)
    else:
        return make_response(jsonify({"msg": "Error", "code": 400}), 400)

# API para guardar censado
@api_persona.route("/persona/guardar/censado", methods=['POST'])
@expects_json(schema)
def guardar_censado():
    data = request.get_json()
    
    id = personaC.guardar_censado(data)
    print("el id es: "+ str(id))
    
    if id >= 0:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag": "Datos Guardados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Erros.error[str(id)]}}), 
            400
        )

schema_censador = {
    "type": "object",
    'properties': {
        "nombres": {"type": "string"},
        "apellidos": {"type": "string"},
        "fecha_nac": {"type": "string"},
        "estado": {"type": "boolean"},
        "correo": {
            "type": "string",
            "pattern": r"^[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}$"
        },
        "clave": {"type": "string"},
    },
    'required': ["nombres", "apellidos", "fecha_nac", "estado", "correo", "clave"]
}

# API para guardar censador
@api_persona.route("/persona/guardar/censador", methods=['POST'])
@expects_json(schema_censador)
def guardar_censador():
    data = request.get_json()
    
    id = personaC.guardar_censador(data)
    print("el id es: "+ str(id))
    
    if id >= 0:
        return make_response(
            jsonify({"msg": "OK", "code": 200, "datos": {"tag": "Datos Guardados"}}),
            200
        )
    else:
        return make_response(
            jsonify({"msg" : "ERROR", "code" : 400, "datos" :{"error" : Erros.error[str(id)]}}), 
            400
        )

# API para mostrar persona por external_id
@api_persona.route("/persona/<external_id>")
def mostrar(external_id):
    persona = personaC.obtener_por_external_id(external_id)
    if persona:
        return make_response(jsonify({"msg": "OK", "code": 200, "datos": persona.serialize()}), 200)
    else:
        return make_response(jsonify({"msg": "Error", "code": 404, "datos": {"error": "Persona no encontrada"}}), 404)

# API para modificar persona por external_id
@api_persona.route("/personam/<external_id>", methods=['PUT'])
def modificar(external_id):
    data = request.get_json()
    persona = personaC.modificar(external_id, data)
    if persona:
        return make_response(jsonify({"msg": "OK", "code": 200, "datos": persona.serialize()}), 200)
    else:
        return make_response(jsonify({"msg": "Error", "code": 404, "datos": {"error": "Persona no encontrada"}}), 404)