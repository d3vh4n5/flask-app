import sqlite3

def dict_factory(cursor, row):
    dictionary = {}
    for idx, col in enumerate(cursor.description):
        dictionary[col[0]] = row[idx] # idx = index
    return dictionary

def getAllUsers():

    try:
        conn = sqlite3.connect('dblite.db')
        # Configuración para que los resultados se devuelvan como 
        #  diccionarios, de no hacerlo, me devuelve una lista de 
        # tuplas que son mas difíciles de identificar sus datos.
        conn.row_factory = dict_factory
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuarios')
        rows = cursor.fetchall()
        # print(rows)
        return rows
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    
    finally:
        conn.close()


def createTable():
    try:
        conn = sqlite3.connect('dblite.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50) NOT NULL
            );
        ''')

        rows = cursor.fetchall()
        print(rows)
        
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    
    finally:
        conn.close()

def insertUser():
    try:
        conn = sqlite3.connect('dblite.db')
        cursor = conn.cursor()

        usuarios = [
            # Importante poner la coma dentro de la tupla, 
            # sino dará error de cantidad de parámetros
            ('Juan',), 
            ('Angel',),
            ('Hans',),
        ]
        cursor.executemany('INSERT INTO usuarios (nombre) VALUES (?)', usuarios)

        conn.commit() # Importante para que os cambios impacten en la db !!

        rows = cursor.fetchall()
        print(rows)
    except sqlite3.Error as e:
        print(f"Error en la BD: {e}")
    
    finally:
        conn.close()

def sqliteTest():
    createTable()
    insertUser()
    return getAllUsers()


if __name__ == '__main__':
    # createTable()
    # insertUser()
    usuarios = getAllUsers()
    print(usuarios)
    for usuario in usuarios:
        print(usuario['nombre'])