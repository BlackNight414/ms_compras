from marshmallow import Schema, fields, post_load
from app.models import Compra
from datetime import datetime

class ComprasSchema(Schema):
    id: int = fields.Integer()
    producto_id: int = fields.Integer(required=True)
    fecha_compra: datetime = fields.DateTime(load_default=datetime.today())
    direccion_envio: str = fields.String(required=True)
    fecha_eliminacion: datetime = fields.DateTime(dump_only=True)
    observaciones: str = fields.String()

    @post_load
    def deserealizar_compra(self, data, **kwargs):
        return Compra(**data)