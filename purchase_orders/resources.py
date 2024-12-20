from flask import jsonify
from flask_restful import Resource, reqparse


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

class PurchaseOrders(Resource):
    
    parser = reqparse.RequestParser()

    parser.add_argument(
    'id',
    type=int,
    required=True,
    help="informe um id"
    )

    parser.add_argument(
    'description',
    type=str,
    required=True,
    help="informe uma descri"
    )

    def get(self):
        return jsonify(purchase_orders)
        
    def post(self):
        request_data = PurchaseOrders().parser.parse_args()

        purchase_order = {
            'id': request_data['id'],
            'description': request_data ['description'],
            'items': []
        }

        purchase_orders.append(purchase_order)

        return jsonify(purchase_order)

class PurchaseOrdersById(Resource):
    def get(self,id):
        for po in purchase_orders:
            if po["id"] == id:
                return jsonify(po["items"])

        return jsonify({"message": "pedido{}nao encontrado".format(id)})