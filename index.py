from flask import Flask, request, json
from flask_cors import CORS
from utilidades import isNumber, isNegative, getSeed
import metodos
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    nombre = ["hola", "martin"]
    return json.jsonify(nombre)


@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    try:
        req = request.get_json()
        v1 = isNumber(isNegative(int(req['v1'])))
        v2 = isNumber(isNegative(int(req['v2'])))
        a = isNumber(isNegative(int(req['a'])))
        n = isNumber(isNegative(int(req['n'])))
        response = metodos.fibonacci(v1, v2, a, n)
        return json.jsonify(response)
    except ValueError as e:
        return e


@app.route('/congruencialMultiplicativo', methods=['POST'])
def congruencialMultiplicativo():
    try:
        req = request.get_json()
        seed = req['seed']
        a = isNumber(isNegative(int(req['a'])))
        n = isNumber(isNegative(int(req['n'])))
        m = isNumber(isNegative(int(req['m'])))
        #Faltan cotroles, m tiene que ser mayor que seed
        response = metodos.congruencialMultiplicativo(seed, n, a, m)
        return json.jsonify(response)
    except ValueError as e:
        return e