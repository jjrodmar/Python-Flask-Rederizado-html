from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola Don Pepito!"

@app.route("/saludo")
def saludo():
    return "Soy Pepe Gotera"

if __name__ == "__main__":
    app.run()
