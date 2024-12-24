from flask import Blueprint, jsonify
from models.model_prueba import obtener_mensaje

# Crear un blueprint para las rutas relacionadas con 'prueba'
prueba = Blueprint('prueba', __name__)

@prueba.route('/prueba', methods=['GET'])
def prueba_route():
    # Usar el modelo para obtener el mensaje
    mensaje = obtener_mensaje()
    return jsonify(message=mensaje)
