from flask import Flask, request, json
from flask_cors import CORS
from utilidades import isNumber, isNegative, getSeed
import metodos
import monobitsTest
import chiCuadrada
from classMark import runClassMarks
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
        return json.jsonify(
            {'msg': "Lo sentimos, hubo un error."})


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
        return json.jsonify(
            {'msg': "Lo sentimos, hubo un error."})


@app.route('/tests/monobits', methods=['POST'])
def test_monobits():
    try:
        req = request.get_json()
        serie = req['serie']
        resultado = monobitsTest.test(serie)
        return json.jsonify(resultado)
    except Exception as e:
        return json.jsonify(
            {'msg': "Lo sentimos, hubo un error durante el test."})


@app.route('/tests/chicuadrada', methods=['POST'])
def test_chicuadrada():
    try:
        req = request.get_json()
        serie = req['serie']
        k = int(req['k'])
        resultado = chiCuadrada.chiCuadrado(serie, k)
        return json.jsonify(resultado)
    except Exception as e:
        return json.jsonify(
            {'msg': "Lo sentimos, hubo un error durante el test."})

@app.route('/classMarks', methods=['POST'])
def classMarks():
    try:
        req = request.get_json()
        serie = req['serie']
        classMarks = req['classMarks']
        minimum = float(req['minimum'])
        maximum = float(req['maximum'])
        resultado = runClassMarks(classMarks, serie, minimum, maximum)
        return json.jsonify(resultado)
    except Exception as e:
        return json.jsonify(
            {'msg': "Lo sentimos, hubo un error."})
