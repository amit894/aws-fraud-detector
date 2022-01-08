import flask
from files import readCustomers
from flask import request,jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/customer', methods=['GET'])
def home():
    return jsonify(readCustomers())
app.run()
