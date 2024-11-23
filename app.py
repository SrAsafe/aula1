from flask import Flask

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'dercription': 'pedido de compra 1',
        'items': [
            {
                'id': 1,
                'description': 'item do pedido 1',
                'price': 20.99
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello World! alterado"


app.run(port=3000)
