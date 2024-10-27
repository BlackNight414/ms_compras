from flask import Blueprint
from flask import jsonify, make_response, request

from app.models import Compra
from app.services import ComprasService

compras = Blueprint('compras', __name__)

compras_service = ComprasService()

@compras.route('/registrar_compra', methods=['POST'])
def registrar_compra():
    datos_compra = request.get_json()

    try: 
        compra = compras_service.registrar_compra(Compra(**datos_compra))
        resp_data = jsonify({
            'id': compra.id,
            'producto_id': compra.producto_id,
            'fecha_compra': compra.fecha_compra,
            'direccion_envio': compra.direccion_envio 
        })
        return resp_data, 200 # código de estado de compra correcto
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