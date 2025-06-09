# Proyecto Django - Mi Tienda Online

Este es un proyecto desarrollado con **Django**, que simula una tienda online de remeras. El objetivo principal es aplicar los conocimientos adquiridos en el desarrollo backend utilizando Django y Bootstrap para el diseño responsive.

---

## Tecnologías utilizadas

- 🐍 **Python 3.13**
- 🌐 **Django 5.2.1**
- 🎨 **Bootstrap 5.3.3**
- 🗃️ **SQLite** como base de datos
- 📦 Gestión de archivos estáticos y medios

---

## Funcionalidades principales

- Listado dinámico de productos (remeras)
- Detalle individual de cada producto
- Carga y visualización de imágenes
- Navegación entre páginas con `url routing`
- Formulario de contacto con validación
- Diseño responsive con Bootstrap
- Plantillas reutilizables usando `base.html` y `extends`
  
---

## Autor
Gustavo Farías | Desarrollador Backend
- [LinkedIn](https://www.linkedin.com/in/gustavoef)
- [GitHub](https://www.github.com/fariasgustavo313)

## Cómo ejecutar el proyecto localmente

### 1. Clona el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

### 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

### 3. Instala las dependencias
pip freeze > requirements.txt
pip install -r requirements.txt

### 4. Aplica migraciones
python manage.py migrate

### 5. Crea un superusuario (opcional)
python manage.py createsuperuser

### 6. Corre el servidor
python manage.py runserver

## Estructura del proyecto
proyecto_integrador_shop/
│
├── myshop/
│   ├── migrations/
│   ├── static/myshop/
│   │   ├── logo.png
│   │   └── style.css
│   ├── templates/myshop/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── detalle_remera.html
│   │   └── contacto.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── media/
│   └── (imagenes de productos subidas)
├── db.sqlite3
├── manage.py
└── README.md
