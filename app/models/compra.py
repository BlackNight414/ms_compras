from app import db
from datetime import datetime

class Compra(db.Model):

    __tablename__ = 'compras'

    id: int = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column('producto_id', db.Integer, nullable=False)
    fecha_compra: datetime = db.Column('fecha_compra', db.DateTime, nullable=False, default=datetime.today())
    direccion_envio: str = db.Column('direccion_envio', db.String(120), nullable=True) # puede no tener dirección
    fecha_eliminacion: datetime = db.Column('fecha_eliminacion', db.DateTime)
    observaciones: str = db.Column('observaciones', db.Text)