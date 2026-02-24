# Docker
sin la necesidad de crear entornos virtuales en la pc.

## 1. clona el repositorio
> selecciona el directorio para el proyecto, depues clona el repositorio con:
> ```bash
> git clone https://github.com/Alvaro17-max/Tienda-online.git
> ```

# 2. tener instalado [docker desktop](https://www.docker.com/products/docker-desktop/)
> abre la terminal en la aplicación

## 2. levanta el contenedor
> ubicate en el proyecto:
> en windows
> ``` bash
> docker run -it --rm --name tiendaOnline -p 5000:5000 -v ${pwd}:/app -w /app python:3.11-slim bash -c "pip install flask && python app.py"
> ````

## 3. acceder a la pagina
> podes acceder a la pagina web sin la necesidad de levantar el entorno virtual

# docker compose.
> es una alternativa mejor para levantar el repositorio
>  PROXIMAMENTE ...
