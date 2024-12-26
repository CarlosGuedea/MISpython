from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.login.login_model import Usuario

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    datos = request.get_json()

    if not datos or not datos.get("email") or not datos.get("password"):
        return jsonify({"error": "Datos incompletos"}), 400

    # Buscar el usuario en la base de datos
    usuario = Usuario.query.filter_by(email=datos['email']).first()

    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Verificar si la contraseña es correcta
    if usuario.password != datos['password']:
        return jsonify({"error": "Contraseña incorrecta"}), 401

    # Crear el token de acceso
    access_token = create_access_token(identity=str(usuario.id))

    # Crear una respuesta antes de establecer la cookie
    response = make_response(jsonify({"message": "Inicio de sesión exitoso"}))

    # Configurar la cookie
    response.set_cookie(
        "access_token",        # Nombre de la cookie
        access_token,         # Valor de la cookie
        httponly=True,         # Evita el acceso desde JavaScript
        secure=True,          # Cambiar a True en producción (requiere HTTPS)
        samesite='None',       # Permitir el acceso cross-origin
        #max_age=50        # Tiempo de vida en segundos (5 minutos)
    )
    return response

@login_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Bienvenido, usuario {current_user}"})
