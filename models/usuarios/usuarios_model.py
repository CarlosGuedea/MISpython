from database.db_usuarios import db_usuarios as db

class Usuario_Local(db.Model):
    __tablename__ = 'usuarios_local'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Usuario {self.email}>"
