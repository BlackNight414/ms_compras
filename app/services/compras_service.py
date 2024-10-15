from app.repositories import ComprasRepository
from app.models import Compra

class ComprasService:

    def __init__(self):
        self.catalogo_repository = ComprasRepository()

    def add(self, compra: Compra):
        return self.catalogo_repository.add(compra)

    def get_by_id(self, id: int):
        return self.catalogo_repository.get_by_id(id)