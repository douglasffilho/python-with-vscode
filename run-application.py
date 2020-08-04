from flask import Flask
from br.com.douglasffilho.controller.product_controller import ProductController

api = Flask(__name__)

ProductController(api)

if __name__ == '__main__':
    api.run()
