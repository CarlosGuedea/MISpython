from flask import Flask, jsonify, make_response
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)

# Configuración global de CORS con soporte para credenciales
CORS(
    app,
    resources={r"/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,  # Permitir envío de cookies y credenciales
)

@app.route('/set-cookie', methods=['GET'])
def set_cookie():
    # Crear una respuesta
    response = make_response(jsonify({"message": "Cookie establecida con éxito"}))

    # Establecer la cookie
    response.set_cookie(
        "access_token",        # Nombre de la cookie
        "12345abcdef",         # Valor de la cookie
        httponly=True,         # Evita el acceso desde JavaScript
        secure=False,          # Cambiar a True en producción (requiere HTTPS)
        samesite='None',       # Permitir el acceso cross-origin
        max_age=300            # Tiempo de vida en segundos (5 minutos)
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
