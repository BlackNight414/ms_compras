from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Compra
from app.services import ComprasService
from app.mapping import ComprasSchema

compras = Blueprint('compras', __name__)

compras_service = ComprasService()
compras_schema = ComprasSchema()

@compras.route('/registrar_compra', methods=['POST'])
def registrar_compra():
    datos = request.get_json()
    try: 
        compra = compras_service.registrar_compra(compras_schema.load(datos))
        return compras_schema.dump(compra), 200
    except BaseException as e:
        print(e)
        return jsonify({'msg': 'Error'}), 500

@compras.route('/eliminar_compra/<int:id_compra>', methods=['DELETE'])
def eliminar_compra(id_compra):
    try:
        observaciones = request.get_json()['observaciones']
        compras_service.eliminar_compra(id_compra, observaciones)
        return jsonify({'msg': f'Compra id={id_compra} eliminada'}, 200)
    except:
        return jsonify({'msg': 'Error'}), 500