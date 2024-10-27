from app.repositories import ComprasRepository
from app.models import Compra

class ComprasService:

    def __init__(self):
        self.compras_repository = ComprasRepository()

    def registrar_compra(self, compra: Compra):
        return self.compras_repository.add(compra)

    def eliminar_compra(self, id_compra: int, observaciones: str = None):
        return self.compras_repository.delete(id_compra, observaciones)

    def get_by_id(self, id: int):
        return self.compras_repository.get_by_id(id)