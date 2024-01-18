from flask import Flask, render_template, jsonify, request
from markupsafe import escape
import pymysql.cursors
from dotenv import load_dotenv
import os
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
        #     cursor.execute(sql, ('juanangelbasgall@hotmail.com',)) # (sql, array de datos)
        #     result = cursor.fetchone()
        #     print(result)
        
        with connection.cursor() as cursor:
            # Read a multiple records
            sql = "SELECT * FROM usuarios"
            # cursor.execute(sql)
            # result = cursor.fetchall()
            # print(result)
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
