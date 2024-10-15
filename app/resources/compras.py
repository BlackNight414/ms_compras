from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Compra
from app.services import ComprasService

compras = Blueprint('compras', __name__)

compras_service = ComprasService()

@compras.route('/add', methods=['POST'])
def add_compra():
    datos_compra = request.get_json()

    compra = Compra(**datos_compra)
    compras_service.add(compra)
    return jsonify({'status_code': 200}) # código de estado de compra correcto