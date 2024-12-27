from flask import Flask
from models.usuarios.usuarios_model import Usuario_Local
from flask_jwt_extended import jwt_required, get_jwt_identity

# Crear un blueprint para el controlador de usuarios
usuario_bp = Blueprint('usuario', __name__)

# Ruta para obtener todos los usuarios
@usuario_bp.route('/usuarios', methods=['GET'])
@jwt_required()  # Proteger la ruta con JWT
def obtener_usuarios():
    usuarios = Usuario_Local.query.all()  # Consultar todos los usuarios
    resultado = [{"id": u.id, "email": u.correo, "password": u.password} for u in usuarios]
    return jsonify(resultado), 200

# Ruta para obtener un usuario por su ID
@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify({"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# Ruta para crear un nuevo usuario
@usuario_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    if not datos or not datos.get("nombre") or not datos.get("email"):
        return jsonify({"error": "Datos incompletos"}), 400

    nuevo_usuario = Usuario(nombre=datos['nombre'], email=datos['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"message": "Usuario creado exitosamente", "id": nuevo_usuario.id}), 201

# Ruta para actualizar un usuario existente
@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"error": "Datos incompletos"}), 400

    usuario.nombre = datos.get('nombre', usuario.nombre)
    usuario.email = datos.get('email', usuario.email)
    db.session.commit()
    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

# Ruta para eliminar un usuario
@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado exitosamente"}), 200

