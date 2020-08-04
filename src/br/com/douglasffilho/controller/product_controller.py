from flask import jsonify


class ProductController:
    def __init__(self, api):
        @api.route('/products')
        def get_all():
            products = [
                {'sku': '1234', 'name': 'Teste'},
                {'sku': '5678', 'name': 'Teste 2'}
            ]
            return jsonify(products)
