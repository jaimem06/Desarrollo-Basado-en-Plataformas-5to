from flask import Blueprint, jsonify, make_response, request
from controllers.personaControl import PersonaControl
api_persona = Blueprint('api_persona', __name__)

# API para Persona
personaC = PersonaControl()
@api_persona.route("/persona")
def listar ():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos":([i.serialize() for i in personaC.listar()])}),
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