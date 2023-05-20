import mysql.connector

def establecer_conexion():
    config = {
        'user': 'root',
        'password': 'Pablo6364',
        'host': 'localhost',
        'database': 'gestionStock'
    }

    conn = mysql.connector.connect(**config)
    return conn