from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import pymysql.cursors
from dotenv import load_dotenv
import os
from db.example_sqlite import sqliteTest
load_dotenv()

# En Desarrollo:
# Ejecutarla con "python flask_app.py" para que refresque
# automaticamente en cada cambio!! Pero tiene que estar
# esta sentencia al final de este archivo:
# if __name__ == "__main__":
#     app.run(debug=True)

# En producción:
#  Ejecuto la app con: flask --app app run
#  o python -m flask --app app run
#  o py -m flask --app app run
#  o py -m flask run

app = Flask(__name__)

errorsito = ''


@app.route("/")
def index():
    context = {
        "error" : errorsito,
        "msj" : "Esto es un mensaje",
        "testVar" : os.environ.get('DB2_HOST', 'loco')
    }
    return render_template("pages/index.html", context = context)

@app.route("/dinamica")
def dinamica():
    # Datos que serán interpolados en el template
    mensaje = "Hola, esto es un mensaje desde el servidor"
    numeros = [1, 2, 3, 4, 5]

    # Pasa los datos al template usando render_template
    return render_template("pages/dinamica.html", mensaje=mensaje, numeros=numeros)


@app.route("/parametro/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# Rutas de Testing:

@app.route("/test", methods=['POST', 'GET'])
def test():
    variableEnvTest = os.environ.get('ENV_VAR', 'Esta no es una variable de entorno')
    if request.method == 'POST':
        print('Hubo un post')
        usuarios = sqliteTest()
        print(usuarios)
        return render_template('pages/test.html', usuarios=usuarios)
    return render_template('pages/test.html', variableEnvTest=variableEnvTest)

@app.route('/fuera-del-formulario', methods=['POST'])
def fuera_del_formulario():
    # Manejar la solicitud AJAX
    data = request.get_json()
    if data and data.get('boton_fuera'):
        print(sqliteTest())
        print('Boton presionado')
        return 'Botón Fuera presionado por AJAX'

    return jsonify({'error': 'Invalid request'})




#########################################
#              API
#########################################

@app.route("/api/data", methods=["GET"])
def get_data():
    # Datos de ejemplo, podrías obtenerlos de una base de datos u otra fuente
    data = {
        "mensaje": "¡Hola, esto es una API!",
        "estado": "éxito",
        "datos": [1, 2, 3, 4, 5]
    }
    return jsonify(data)

@app.route("/contacto", methods = ["POST", "GET"])
def contactHandling():
    diccionario = {
        "nombre": "Juan",
        "edad" : 32,
        "soltero" : True
    }
    consulta = {}
    respuesta = jsonify(diccionario)
    # Permitimos conexion de cualquier lado !!! WARNING Security!
    respuesta.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'POST':
        print("Hubo un post")

        # jsonData = request.get_json() # Esto es si envio datos tipo json
        # print(jsonData['nombre'])
        # print(jsonData['edad'])
        # print(jsonData['soltero'])

        data = request.form # Esto es para el etandar de form-data
        print(data['email'])
        print(data['motivo'])
        print(data['mensaje'])
        # return respuesta
        return "<h1>Información enviada correctamente!</h1>"
    return render_template('pages/contacto.html')






# Importante para que en algunos entornos ejecute la aplicaciones
# Dependiendo donde esté desplegado
if __name__ == "__main__":
    app.run(debug=True)

