from flask import Flask
from flask_cors import CORS  # Importar CORS
from controllers.usuarios.usuarios_controller import usuario_bp
from controllers.login.login_controller import login_bp
from controllers.requisitos_crud.requisitos_controller import requisitos_bp
from database.db_usuarios import init_db
from flask_jwt_extended import JWTManager
from authlib.integrations.flask_oauth2 import AuthorizationServer
from controllers.usuarios_perfil.usuarios_perfil import perfil_bp



app = Flask(__name__)

# Configuración de CORS con soporte para credenciales
CORS(app, resources={r"/prueba": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/saludo/*": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/login": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/protected": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/token": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/requisitos": {"origins": "http://localhost:5173", "supports_credentials": True}})
CORS(app, resources={r"/requisitos/*": {"origins": "http://localhost:5173", "supports_credentials": True}})

#CORS para el frontend
CORS(app, resources={r"/prueba": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/saludo/*": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/login": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/protected": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/token": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/requisitos": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})
CORS(app, resources={r"/requisitos/*": {"origins": "https://misalfa.netlify.app", "supports_credentials": True}})


# Registrar las rutas desde los controladores
app.register_blueprint(usuario_bp)
app.register_blueprint(login_bp)
app.register_blueprint(perfil_bp)
app.register_blueprint(requisitos_bp)

# Inicializar la base de datos
init_db(app)

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Clave secreta para firmar los tokens
app.config['JWT_TOKEN_LOCATION'] = ['cookies']  # Configurar para usar cookies
app.config['JWT_COOKIE_SECURE'] = False         # Cambiar a True en producción para usar HTTPS
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False   # Habilitar protección CSRF si es necesario
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWTManager(app)

# Configura el servidor OAuth2
authorization = AuthorizationServer(app)

if __name__ == '__main__':
    app.run(debug=True)
