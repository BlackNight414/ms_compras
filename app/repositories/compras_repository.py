from app import db
from app.models import Compra
from datetime import datetime

class ComprasRepository:

    def add(self, compra: Compra):
        """ Registra una compra """
        db.session.add(compra)
        db.session.commit()
        return compra

    def delete(self, id_compra: int, observaciones: str = None):
        """ Soft delete: agrega una fecha de eliminacion a una compra y observaciones de por qué se 'elimina' """
        compra = self.get_by_id(id_compra)
        if compra:
            compra.fecha_eliminacion = datetime.now() 
            compra.observaciones = observaciones
            db.session.add(compra)
            db.session.commit()
            return compra
        else:
            raise f'Compra con id={id_compra} no existe.'

    def get_by_id(self, id: int):
        """ Obtiene una compra por su id """
        return db.session.query(Compra).filter(Compra.id==id).first()

