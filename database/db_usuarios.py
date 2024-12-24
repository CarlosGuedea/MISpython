from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Crear una instancia de SQLAlchemy
db_usuarios = SQLAlchemy()

def init_db(app: Flask):
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mssql+pyodbc://carlos2025:1231#ASDF!a@vuamm1.database.windows.net:1433/usuarios?driver=ODBC+Driver+17+for+SQL+Server'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar el seguimiento de modificaciones
    db_usuarios.init_app(app)
