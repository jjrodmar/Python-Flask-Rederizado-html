'''from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Don Pepito!"

@app.route("/saludo")
def saludo():
    return "Soy Pepe Gotera"

@app.route("/edit")
def responder():
    return "Hola Don Jose"


if __name__ == "__main__":
    app.run()
'''
import pymysql
from ClaseConect import *
from flask import Flask, request, jsonify, render_template, redirect
#from markupsafe import Markup, escape


app = Flask(__name__)

@app.route("/")
def hello():
    return redirect('/list')
   # return "Hola Don Pepito!"
'''@app.route("/<name>")
def helloName(name):
    return "Hola Don "+str(name)'''



# SIN renderizar 
@app.route("/all")
def todos():
    claseConn=ClaseConect()
    claseConn.EjecutarSql("select * from personal")
    datos=claseConn.DevolverTodos()
    resp=jsonify(datos)
    resp.status_code=200
    claseConn.CerrarConect()
    return resp

# renderizando
@app.route("/list")
def list():
    claseConn=ClaseConect()
    claseConn.EjecutarSql("select * from personal")
    datos=claseConn.DevolverTodos()
    #datos.status_code=200
    claseConn.CerrarConect()
    
    return render_template('index.html', datos=datos)
   



@app.route('/<id>')
def userId(id):
    
    claseConn=ClaseConect()
    claseConn.EjecutarSql("select * from personal where id=" + id )
    datos=claseConn.DevolverTodos()
    resp=jsonify(datos)
    resp.status_code=200
    claseConn.CerrarConect()
    return resp   

@app.route("/add")
def AltasAdd():
    return render_template('add.html')


#ALTAS @app.route('/<int:year>/<int:month>/<title>')
# def article(year, month, title):
@app.route("/add", methods=["POST"])
def Altas():
    try:
        claseConn=ClaseConect()
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        claseConn.EjecutarSql("insert into personal (nombre, apellido) values ('"+ str(nombre)+ "','"+ str(apellido)+"')" )
        datos = claseConn.DevolverUno()
        claseConn.RealizaCambios()
        print(datos)
    except Exception:
        claseConn.DeshaceCambios
        print("Error en las Altas")
        #(e)
    
    return redirect("/list")
   
  

@app.route("/edit", methods=["GET","POST"])
def edit():
    try:
        claseConn=ClaseConect()
        id=request.form.get("id")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        claseConn.EjecutarSql("update personal set nombre='" + str(nombre)+ "', apellido='"+ str(apellido)+"' where id="+str(id) )
        datos = claseConn.DevolverUno()
        claseConn.RealizaCambios()
        print(datos)
    except Exception:
        claseConn.DeshaceCambios()
        print("Error en las Modificaciones")
        #(e)
    return redirect("/list")

@app.route("/delete/<id>", methods=["GET","POST"])
def delete(id):

    try:
        claseConn=ClaseConect()
        claseConn.EjecutarSql("delete from personal where id="+str(id) )
        datos = claseConn.DevolverUno()
        #gdgdghdj
        
        claseConn.RealizaCambios()
        print(datos)
    except Exception:
        claseConn.DeshaceCambios()
        print("Error en las Bajas")
        #(e)
    return redirect("/list")

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
    #app.run(debug=True, host='0.0.0.0', port=8000)
    app.run(debug=True)
