from flask import Flask, Blueprint, jsonify
from models.requisitos.requisitos_model_read import Requisitos_Read
from models.requisitos.requisitos_model_detalle import Requisitos_Detalle
from models.requisitos.requisitos_model_seccion import Requisitos_Seccion
from flask_jwt_extended import jwt_required, get_jwt_identity

# Crear un blueprint para el controlador de usuarios
requisitos_bp = Blueprint('requisitos', __name__)

# Ruta para obtener todos los usuarios
@requisitos_bp.route('/requisitos', methods=['GET'])
@jwt_required()  # Proteger la ruta con JWT

def Requisitos_Listar():
    Requisitos = Requisitos_Read.obtener_requisitos()
    # Consultar todos los requisitos
    resultado = [
        {
            "id": u.id,
            "estatus": u.estatus,
            "codigo": u.codigo,
            "requisito": u.valor,
            "etiqueta": u.etiqueta
        }
        for u in Requisitos  # Itera sobre cada objeto en la lista
    ]
    return jsonify(resultado), 200

from flask_jwt_extended import jwt_required
from flask import jsonify

#Ruta para obtener los detalles de los requisitos
@requisitos_bp.route('/requisitos/<int:id>', methods=['GET'])
@jwt_required()
def obtener_requisito_y_seccion(id):
    try:
        # Llamada a las funciones que obtienen los datos
        requisito = obtener_requisito(id)
        seccion = obtener_seccion(id)

        # Verifica si ambos resultados están siendo devueltos correctamente
        if 'error' not in requisito and 'error' not in seccion:
            resultado = {
                "requisito": requisito,
                "seccion": seccion
            }
            return jsonify(resultado)
        else:
            return jsonify({"error": "No se encontraron los datos del requisito o sección"}), 404

    except Exception as e:
        return jsonify({"error": f"Error al procesar la solicitud: {str(e)}"}), 500

def obtener_requisito(id):
    try:
        # Lógica para obtener el requisito
        requisito = Requisitos_Detalle.obtener_requisitos_detalle(id)
        if requisito:
            return {
                "id": requisito.id,
                "estatus": requisito.estatus,
                "codigo": requisito.codigo,
                "requisito": requisito.valor,
                "etiqueta": requisito.etiqueta,
                "descripcion": requisito.descripcion,
            }
        else:
            return {"error": "Requisito no encontrado"}
    except Exception as e:
        return {"error": f"Error al obtener el requisito: {str(e)}"}

def obtener_seccion(id):
    try:
        # Lógica para obtener la sección
        seccion = Requisitos_Seccion.obtener_secciones_detalle(id)
        if seccion:
            return {
                "id_requisito": seccion.id_requisito,
                "descripcion_requisito": seccion.descripcion_requisito,
                "cat_id": seccion.cat_id,
                "valor": seccion.valor,
                "descripcion_seccion": seccion.descripcion_seccion,
            }
        else:
            return {"error": "Sección no encontrada"}
    except Exception as e:
        return {"error": f"Error al obtener la sección: {str(e)}"}

# Ruta para crear un nuevo usuario
@requisitos_bp.route('/usuarios', methods=['POST'])
def crear_requisito():
    datos = request.get_json()
    if not datos or not datos.get("nombre") or not datos.get("email"):
        return jsonify({"error": "Datos incompletos"}), 400

    nuevo_usuario = Usuario(nombre=datos['nombre'], email=datos['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"message": "Usuario creado exitosamente", "id": nuevo_usuario.id}), 201

# Ruta para actualizar un usuario existente
@requisitos_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_requisito(id):
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
@requisitos_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_requisito(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado exitosamente"}), 200

