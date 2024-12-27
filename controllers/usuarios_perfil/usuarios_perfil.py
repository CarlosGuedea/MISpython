from flask import Blueprint, jsonify
from models.login.usuarios_perfil_model import Usuarios_Perfil

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/perfiles', methods=['GET'])
def obtener_perfiles():
    try:
        # Usar el nombre correcto de la clase
        # Obtener los perfiles de un usuario específico (por ejemplo, usuario_id=124)
        perfiles_lista = Usuarios_Perfil.obtener_perfiles_por_usuario_id(124)

        return jsonify(perfiles_lista), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
