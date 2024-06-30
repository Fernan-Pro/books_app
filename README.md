# Proyecto Books App

Este proyecto es una aplicación web para la gestión de libros, construida con un backend en Django.

## Características

- Añadir, actualizar y eliminar libros.
- Ver detalles de cada libro.
- Interfaz de usuario simple y fácil de usar.

## Requisitos

- Python 3.x
- Node.js y npm (si se usa React o algún frontend avanzado)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/Fernan-Pro/books_app.git
   cd books_app
   ```

2. Instala las dependencias del backend:

   ```bash
   cd server_web
   pip install -r requirements.txt
   ```

## Uso

1. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

2. Inicia el servidor backend:

   ```bash
   python manage.py runserver
   ```

3. Abre tu navegador y navega a `http://localhost:8000` para usar la aplicación.

## Estructura del Proyecto

```plaintext
.
├── README.md
├── server_web
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
├── books
│   ├── models.py
│   └── ...
├── static
│   └── styles
│       └── bootstrap.min.css
└── db.sqlite3
```

- `server_web`: Contiene el código y dependencias del servidor backend hecho con Django.
- `books`: Contiene la lógica de la aplicación relacionada con los libros.
- `static`: Contiene los archivos estáticos como CSS.
- `db.sqlite3`: Archivo de la base de datos SQLite.

## Contacto

Para cualquier consulta o sugerencia, puedes contactarme a través de ferqtexwinner@gmail.com.
