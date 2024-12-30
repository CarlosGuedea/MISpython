from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Requisito(db.Model):
    __tablename__ = 'cat_requisitos'  # Asegúrate de que el nombre de la tabla sea correcto

    id = db.Column(db.Integer, primary_key=True)
    estatus = db.Column(db.Boolean, nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    requisito = db.Column(db.String(255), nullable=False)
    etiqueta = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def __init__(self, estatus, codigo, requisito, etiqueta, descripcion):
        self.estatus = estatus
        self.codigo = codigo
        self.requisito = requisito
        self.etiqueta = etiqueta
        self.descripcion = descripcion

    def update(self, estatus, codigo, requisito, etiqueta, descripcion):
        self.estatus = estatus
        self.codigo = codigo
        self.requisito = requisito
        self.etiqueta = etiqueta
        self.descripcion = descripcion

    def to_dict(self):
        return {
            "id": self.id,
            "estatus": self.estatus,
            "codigo": self.codigo,
            "requisito": self.requisito,
            "etiqueta": self.etiqueta,
            "descripcion": self.descripcion,
        }
