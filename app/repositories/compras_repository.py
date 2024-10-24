from app import db
from app.models import Compra

class ComprasRepository:

    def add(self, compra: Compra):
        """ Registra una compra """
        db.session.add(compra)
        db.session.commit()
        return compra

    def delete(self, id_compra: int):
        compra = self.get_by_id(id_compra)
        if compra:
            db.session.delete(compra)
            db.session.commit()
        else:
            raise f'Compra con id={id_compra} no existe.'

    def get_by_id(self, id: int):
        """ Obtiene una compra por su id """
        return db.session.query(Compra).filter(Compra.id==id).first()

