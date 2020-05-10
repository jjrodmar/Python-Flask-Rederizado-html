'''from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Don Pepito!"

@app.route("/saludo")
def saludo():
    return "Soy Pepe Gotera"

if __name__ == "__main__":
    app.run()
'''
import pymysql
from classconect import *
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/todos")
def user():
    claseConn=ClaseConect()
    claseConn.EjecutarSql("select * from personal")
    datos=claseConn.DevolverTodos()
    resp=jsonify(datos)
    resp.status_code=200
    claseConn.CerrarConect()
    return resp
   
@app.route("/saludo")
def saludo():
    return "Hola Don Pepito"

@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message': 'Not Found:'+request.url
        }
    resp= jsonify(message)
    resp.status_code=404
    return resp

if __name__ == "__main__":
    app.run()
