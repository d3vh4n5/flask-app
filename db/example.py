import pymysql

conn = pymysql.connect(host=credentials.HOST, user=credentials.USER, passwd=credentials.PASSWRD, db=credentials.DATABASE)
cur = conn.cursor()
cur.execute('USE USERNAME$DATEBASE')
sql = """SELECT *
            FROM table1
            LIMIT 1"""
cur.execute(sql)
cur.connection.commit()
variable = cur.fetchall()