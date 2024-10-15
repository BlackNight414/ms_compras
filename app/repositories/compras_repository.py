from app import db
from app.models import Compra

class ComprasRepository:

    def add(self, compra: Compra):
        """ Registra una compra """
        db.session.add(compra)
        db.session.commit()
        return compra

    def get_by_id(self, id: int):
        """ Obtiene una compra por su id """
        return db.session.query(Compra).filter(Compra.id==id).first()

