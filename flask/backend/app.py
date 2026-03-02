from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)  

#crear coneccion a la base de datos MySQL
dbDatos ={
    host="localhost",
    user="root",
    password="mysql",
    database="tiendaOnline",
    port=3306
}

print("Conexión exitosa a MySQL!")

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    data = request.get_json()
    nombre = data.get('nombre')
    contrasena = data.get('contrasena') 

    conexion = mysql.connector.connect(**dbDatos)
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (nombre, contrasena) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, contrasena))
    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({'message': 'Registration successful'}), 201 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
