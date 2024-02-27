#!/usr/bin/python3
"""register the blueprint app_views to your Flask instance app"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def sto(exception):
    """method to handle @app.teardown_appcontext
    that calls storage.close()"""

    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a JSON-formatted
    404 status code response"""

    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)
