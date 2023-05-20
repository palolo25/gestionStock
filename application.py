from flask import Flask, render_template, request
import mysql.connector
from establishConexion import establecer_conexion

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('home/index.html')

# Ruta para procesar las consultas
@app.route('/consulta', methods=['POST'])
def consulta():
    # Obtener los datos de la consulta desde el formulario
    operacion = request.form.get('operacion')
    tabla = request.form.get('tabla')
    parametros = request.form.get('parametros')

    # Establecer la conexión a la base de datos
    conn = establecer_conexion()

    # Ejecutar la consulta según la operación seleccionada
    cursor = conn.cursor()

    if operacion == 'CREATE':
        # Ejecutar consulta de inserción (CREATE)
        query = f'INSERT INTO {tabla} VALUES ({parametros})'
        cursor.execute(query)
        conn.commit()
        mensaje = 'Registro insertado con éxito'

    elif operacion == 'READ':
        # Ejecutar consulta de lectura (READ)
        query = f'SELECT * FROM {tabla}'
        cursor.execute(query)
        results = cursor.fetchall()
        mensaje = None  # No se muestra mensaje en caso de lectura

        # Procesar los resultados de la consulta
        processed_results = []

        for row in results:
            processed_row = {
                'campo1': row[0],
                'campo2': row[1],
                # ...
            }

            processed_results.append(processed_row)

        return render_template('home/resultados.html', results=processed_results)

    elif operacion == 'UPDATE':
        # Ejecutar consulta de actualización (UPDATE)
        query = f'UPDATE {tabla} SET {parametros}'
        cursor.execute(query)
        conn.commit()
        mensaje = 'Registro(s) actualizado(s) con éxito'

    elif operacion == 'DELETE':
        # Ejecutar consulta de eliminación (DELETE)
        query = f'DELETE FROM {tabla} WHERE {parametros}'
        cursor.execute(query)
        conn.commit()
        mensaje = 'Registro(s) eliminado(s) con éxito'

    # Cerrar la conexión
    conn.close()

    return render_template('home/index.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run()