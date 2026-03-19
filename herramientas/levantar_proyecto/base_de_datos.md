# BASE DE DATOS

## 1. instalar MYSQL o MARIADB localmente
``` bash
sudo apt upgrade -y
sudo apt install mariadb-server -y
```

## 2. verificar que esta disponible
``` bash
sudo systemctl start mysql
sudo systemctl status mariadb
```

## 3. configuracion inicial
``` bash
sudo mysql_secure_installation
```

## 4. crear usuarui y dar permisos para utilizar 
```bash
sudo mysql
CREATE USER 'tuusuario'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PPTIVILEGES *.* TO 'tuusuario'@'localhost' IDENTIFIED BY 'contraseña';
FLUSK PRIVILEGES;
```

ahora puede acceder con `mysqll -u tuusuario -p`

## 5. crea la base de datos.
``` mysql
CREATE DATABASE tienda_online_db;
USE tienda_online_db;
```
