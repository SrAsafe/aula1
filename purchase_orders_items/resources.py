from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        "id": 1,
        "description": "Purchase Order id 1",
        "items": [{"id": 1, "description": "Item do pedido 1", "price": 19.99}],
    }
]


class PurchaseOrdersItems(Resource):

    def get(self, id):
        for po in purchase_orders:
            if po["id"] == id:
                return jsonify(po["items"])
            return jsonify({"message": "pedido de id{} n encontrado".format(id)})
