import mysql.connector


#connectando-se ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="dateandre",
    database="curso"
)
cursor = db.cursor()


def inserir(name,password):
    sql = "INSERT INTO testes (usuario, senha) VALUES (%s, %s)"
    cursor.execute(sql, (name, password))
    db.commit()



