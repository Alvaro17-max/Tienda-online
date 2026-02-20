<h1 align="center">Crea tú entorno virtual</h1>

## Vale para el frontend

1. crea tu carpeta con:

```bash
  python3 -m venv .venv
```

2. activa el entorno:
   
```bash
   source .venv/bin/activate
```

3. instala flask dentro del entorno:

```bash
   pip install flask
```

4. verifica si se instalo:

```bash
  pip list
```

> ## Crea tu archivo
> app.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=5000)
```

> index.html

```html
<!DOCTYPE  html>
<html lang="es">
<head>
  <title>mi primera pagina</title>
</head>
<body>
  <p>Hola, mundo</p>
</body>
</html>
```
> ## Ejecuta tu proyecto

```bash
  python3 app.py
```

> ## Desactiva el entorno
```bash
  deactivate
```
