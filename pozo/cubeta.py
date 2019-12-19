from flask import Flask
from pozo.vista import principal



def agua()->Flask:
    app = Flask(__name__)
    app.register_blueprint(principal.bp)
    return app