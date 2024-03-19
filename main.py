from flask import Flask, jsonify, request, redirect
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'dbname': 'bzvpsdcz',
    'user': 'bzvpsdcz',
    'password': '0RmfG9N5OyThBp8SC1oxQEnGin-bNjx5',
    'host': 'isabelle.db.elephantsql.com'
}

# Función para obtener todos los clientes
def listar_clientes():
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM clientes;')
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleados

# Función para obtener todos los empleados
def listar_empleados():
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM empleados;')
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleados

# Función para obtener todos los productos
def listar_productos():
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM productos;')
    empleados = cursor.fetchall()
    cursor.close()
    connection.close()
    return empleados

# Ruta para obtener todos los clientes en formato JSON
@app.route('/api/clientes', methods=['GET'])
def mostrar_clientes():
    clientes = listar_clientes()
    return jsonify({'clientes': clientes})

# Ruta para obtener todos los empleados en formato JSON
@app.route('/api/empleados', methods=['GET'])
def mostrar_empleados():
    empleados = listar_empleados()
    return jsonify({'empleados': empleados})

# Ruta para obtener todos los productos en formato JSON
@app.route('/api/productos', methods=['GET'])
def mostar_productos():
    productos = listar_productos()
    return jsonify({'productos': productos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)









