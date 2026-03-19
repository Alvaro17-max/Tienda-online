from flask import Flask, jsonify, request
from base_datos.conexion import conectar_mysql

app = Flask(__name__)  

@app.route('/api/registrar', methods=['POST'])
def registrar_usuario():

    nombre = request.form.get('nombre')
    dni = request.form.get('dni')
    apellido = request.form.get('apellido')
    email = request.form.get('email')
    contrasena = request.form.get('password') 
     
    if not all([nombre, dni, apellido, email, contrasena]):
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400
    
    conexion, cursor = conectar_mysql()
    try:
        nuevos_datos = "INSERT INTO usuario (nombre, dni, apellido, email, contrasena) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(nuevos_datos, (nombre, dni, apellido, email, contrasena))
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
