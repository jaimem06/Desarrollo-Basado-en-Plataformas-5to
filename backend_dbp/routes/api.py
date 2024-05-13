from flask import Blueprint, jsonify, make_response, request

# Importacion de los modelos de tablas de la base de datos
from models.rol import Rol
from models.catalogo_motivo import Catalogo_Motivo
from models.censo_persona import Censo_Persona
from models.censo import Censo
from models.motivo import Motivo
from models.persona import Persona
from models.cuenta import Cuenta


api = Blueprint('api', __name__)

@api.route("/")
def home ():
    return make_response(
        jsonify({"msg": "OK", "code": 200}),
        200
    )