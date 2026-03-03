from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)  

#crear conexion a la base de datos MySQL
dbDatos ={
    "host": "db",
    "user": "root",
    "password": "mysql",
    "database": "tiendaOnline",
    "port": 3306
}

@app.route('/api/registrar', methods=['POST'])
def registrar_usuario():

    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    contrasena = request.form.get('password') 

    try:
        conexion = mysql.connector.connect(**dbDatos)
        cursor = conexion.cursor()
        print("Conexión a MySQL exitosa")
        
    except mysql.connector.Error as e:
        print("Error al conectar a MySQL:", e)
        return jsonify({'error': 'No se pudo conectar a la base de datos'}), 500

    try:
        sql = "INSERT INTO usuario (nombre, apellido, email, contrasena) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, apellido, email, contrasena))
        conexion.commit()
    except mysql.connector.Error as e:
        print("Error al insertar en MySQL:", e)
        return jsonify({'error': 'No se pudo registrar el usuario'}), 500
    finally:
        cursor.close()
        conexion.close()

    return jsonify({'message': 'Registro exitoso'}), 201 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
