from flask import Blueprint, request, jsonify
from models.saludo_model import obtener_saludo

# Crear un blueprint para las rutas relacionadas con 'saludo'
saludo = Blueprint('saludo', __name__)

@saludo.route('/saludo/<nombre>', methods=['GET'])
def saludo_route(nombre):
    # Usar el modelo para obtener el saludo
    saludo_personalizado = obtener_saludo(nombre)
    return jsonify(message=saludo_personalizado)
