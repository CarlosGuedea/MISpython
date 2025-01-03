from flask import Flask, Blueprint, jsonify, request
from datetime import datetime
import uuid
from models.requisitos.requisitos_model_read import Requisitos_Read
from models.requisitos.requisitos_model_detalle import Requisitos_Detalle
from models.requisitos.requisitos_model_seccion import Requisitos_Seccion
from models.requisitos.requisitos_model_update import Requisitos_Update
from models.requisitos.requisitos_model_seccion_update import Seccion_Update
from models.requisitos.requisitos_model_nuevo import Requisitos_Nuevo
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


# Ruta para crear un nuevo requisito
@requisitos_bp.route('/requisitos-nuevo', methods=['POST'])
@jwt_required()
def crear_requisito():
    try:
        data = request.json
        print(data)
        # Validar datos requeridos
        if not data.get("requisito") or not data.get("seccion"):
            return jsonify({"error": "Datos incompletos"}), 400

        # Extraer datos del frontend
        requisito = data["requisito"]
        seccion = data["seccion"]

        # Generar campos predeterminados
        uuid_requisito = str(uuid.uuid4())
        fecha_actual = datetime.now()
        id_area = 1  # Asignar un valor predeterminado
        id_tarifa = 1  # Asignar un valor predeterminado
        activo = 1
        estatus = 1
        fila = 1
        tipo = "R"
        usuario_creado = 1  # Se puede obtener del usuario autenticado

        # Llamar al método del modelo
        resultado = Requisitos_Nuevo.nuevo_requisitos(
            uuid=uuid_requisito,
            id_area=id_area,
            valor=requisito["requisito"],
            etiqueta=requisito["etiqueta"],
            codigo=requisito["codigo"],
            descripcion=requisito["descripcion"],
            id_tarifa=id_tarifa,
            activo=activo,
            estatus=estatus,
            usuario_creado=usuario_creado,
            fecha_creado=fecha_actual,
            fecha_eliminado=None,
            tipo=tipo,
            valor_seccion=seccion["nombre"],
            descripcion_seccion=seccion["descripcion"],
            fila=fila,
            activo_seccion=activo,
            estatus_seccion=estatus,
            usuario_creado_seccion=usuario_creado,
            fecha_creado_seccion=fecha_actual,
            fecha_eliminado_seccion=None,
        )

        if resultado:
            return jsonify({"message": "Requisito y sección creados exitosamente"}), 200
        else:
            return jsonify({"error": "No se pudo crear el requisito"}), 500

    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500



# Ruta para actualizar un usuario existente
@requisitos_bp.route('/requisitos/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_requisito(id):
    try:
        # Obtener los datos de la solicitud
        data = request.get_json()
        codigo = data.get("codigo")
        requisito = data.get("requisito")
        descripcion = data.get("descripcion")

        # Validar que todos los campos requeridos estén presentes
        if not all([codigo, requisito, descripcion]):
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        # Llamar al modelo para realizar la actualización
        actualizado = Requisitos_Update.update_requisitos(
            id, codigo, requisito, descripcion
        )

        if actualizado:
            return jsonify({"mensaje": "Requisito actualizado exitosamente"}), 200
        else:
            return jsonify({"error": "No se encontró el requisito con el ID proporcionado"}), 404

    except Exception as e:
        return jsonify({"error": f"Error al procesar la solicitud: {str(e)}"}), 500


@requisitos_bp.route('/requisitos-seccion/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_seccion(id):
    try:
        # Obtener los datos de la solicitud
        data = request.get_json()
        valor = data.get("valor")
        descripcion_seccion = data.get("descripcion_seccion")

        # Validar que todos los campos requeridos estén presentes
        if not all([valor, descripcion_seccion]):
            return jsonify({"error": "Faltan datos obligatorios"}), 400

        # Llamar al modelo para realizar la actualización
        actualizado = Seccion_Update.actualizar_seccion(
            id, valor, descripcion_seccion
        )

        if actualizado:
            return jsonify({"mensaje": "Seccion actualizada exitosamente"}), 200
        else:
            return jsonify({"error": "No se encontró la seccion con el ID proporcionado"}), 404

    except Exception as e:
        return jsonify({"error": f"Error al procesar la solicitud: {str(e)}"}), 500


# Ruta para eliminar un usuario
@requisitos_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_requisito(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado exitosamente"}), 200

