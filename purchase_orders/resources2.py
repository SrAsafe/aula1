from flask_restful import Resource
from flask import jsonify

purchase_orders = [
    {
        'id':1,
        'description':'pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description':'item do pedido 1',
                'price': 20.99
            }
        ]        
    }
]

class PurchaseOrdersItems(Resource):
    def get(self):
        for po in purchase_orders:
            if po ['id'] == id:
                return jsonify (po['items'])
        
        return jsonify({"message": "pedido{}nao encontrado".format(id)})