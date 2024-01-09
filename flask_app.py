from flask import Flask, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

#  Ejecuto la app con: flask --app app run
#  o python -m flask --app app run
#  o py -m flask --app app run
#  o py -m flask run


@app.route("/")
def index():
    return"<h1>Esto es una app en Flask</h1>"

@app.route("/dinamica")
def dinamica():
    # Datos que serán interpolados en el template
    mensaje = "Hola, esto es un mensaje desde el servidor"
    numeros = [1, 2, 3, 4, 5]

    # Pasa los datos al template usando render_template
    return render_template("dinamica.html", mensaje=mensaje, numeros=numeros)


@app.route("/parametro/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/page")
def pagina():
    return render_template('./pagina.html')

@app.route("/api/data", methods=["GET"])
def get_data():
    # Datos de ejemplo, podrías obtenerlos de una base de datos u otra fuente
    data = {
        "mensaje": "¡Hola, esto es una API!",
        "estado": "éxito",
        "datos": [1, 2, 3, 4, 5]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

