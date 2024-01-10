from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import pymysql.cursors
from dotenv import load_dotenv
import os
load_dotenv()
#  Ejecuto la app con: flask --app app run
#  o python -m flask --app app run
#  o py -m flask --app app run
#  o py -m flask run

app = Flask(__name__)

errorsito = 'Estado: declarado - Original'

try:

    # https://pypi.org/project/pymysql/
    connection = pymysql.connect(host=os.environ.get('DB2_HOST', 'loco'),
                                user=os.getenv('DB2_USER'),
                                password=os.getenv('DB2_PASS'),
                                database=os.getenv('DB2_NAME'),
                                cursorclass=pymysql.cursors.DictCursor)

    with connection:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT `id`, `nombre` FROM `usuarios` WHERE `email`=%s"
        #     cursor.execute(sql, ('juanangelbasgall@hotmail.com',))
        #     result = cursor.fetchone()
        #     print(result)
        
        with connection.cursor() as cursor:
            # Read a multiple records
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
except Exception as e:
    print("Se enconro un error: ")
    print(e)
    errorsito = e


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

@app.route("/page")
def pagina():
    return render_template('pages/pagina.html')





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
        data = request.form
        print(data['email'])
        print(data['motivo'])
        print(data['mensaje'])
        return respuesta
    return render_template('pages/contacto.html')







if __name__ == "__main__":
    app.run(debug=True)

