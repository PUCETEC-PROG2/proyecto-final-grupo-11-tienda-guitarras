[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/p9VNMUI0)
# Trabajo integrador de segundo semestre
El objetivo de este trabajo integrador es proporcionar a los estudiantes de segundo nivel de desarrollo de software una experiencia práctica que combine los conocimientos adquiridos en los cursos de Programación II y Bases de Datos I. A través de este proyecto, los estudiantes desarrollarán una aplicación web utilizando Django, HTML, CSS y JavaScript, aplicando principios de la programación orientada a objetos y el modelo vista-controlador. Además, implementarán una base de datos relacional en PostgreSQL, diseñando el diagrama lógico, creando las tablas con sus respectivas relaciones y validando la integridad de los datos mediante restricciones y llaves.

Este trabajo integral permite a los estudiantes aplicar y consolidar sus conocimientos en dos áreas fundamentales del desarrollo de software: la programación y la gestión de bases de datos. Los estudiantes deberán desarrollar un catálogo temático que integre los conocimientos de ambas asignaturas, mediante el análisis y desarrollo de la gestión de productos y compras, y generación de reportes.

La implementación completa de este proyecto demostrará la capacidad de los estudiantes para desarrollar aplicaciones robustas y eficientes, conectadas a una base de datos relacional, fortaleciendo así su preparación para desafíos profesionales futuros.

## Nombres de los estudiantes

<Ingresar aquí los nombres de los estudiantes>

## Objetivos 

### 1. Reconocimiento y Aplicación de Conceptos Básicos de POO
El estudiante debe demostrar su capacidad para reconocer y aplicar conceptos fundamentales del Paradigma Orientado a Objetos (POO) tales como clases, objetos, atributos y métodos.

### 2. Desarrollo de Aplicaciones Web con Django
Este proyecto servirá como una introducción al desarrollo de aplicaciones web mediante el uso de Django como framework. El estudiante debe ser capaz de utilizar modelos en Django para reforzar sus conocimientos sobre POO y el manejo de bases de datos relacionales.

### 3. Diseño de Interfaces Gráficas Web
El estudiante debe ser capaz de desarrollar interfaces gráficas web utilizando HTML y CSS, mostrando un entendimiento sólido de cómo construir y estilizar páginas web de manera efectiva.


## Requerimientos
Programación II
En cuanto al programa deberá estar desarrollado en Django, HTML, CSS y Javascript, y todos los módulos deberán estar implementar programación Orientada a objetos. Se debe también recordar que el programa debe estar implementado sobre un modelo vista controlador.

Requerimientos:
· El programa debe manejar login de usuarios.
· La primera pantalla mostrará los respectivos enlaces y su respectivo logotipo
· Los enlaces de las pantallas de Clientes. Productos y Compras mostrarán una tabla con sus respectivos campos. Se deberá tener un menú desplegable de “Archivo” con un Item “Nuevo registro” que permita ingresar un nuevo registro en la base de datos y que actualizará la tabla de la aplicación
De la misma manera a la derecha de cada registro se tendrá los botones de edición y de eliminación. El primero abrirá el formulario de edición correspondiente y el segundo mostrará un Dialog de confirmación de eliminación.
· La pantalla de productos deberá mostrarse con su respectiva categoría
· Para la pantalla de compras se tendrán las siguientes especificaciones

  - Pantalla inicial: La pantalla inicial mostrará las compras ordenadas decentemente por fecha, con su respectivo cliente. Además deben tener un apartado para ingresar una nueva compra. Además tendra un botón adicional en cada registro que permita ver los detalles de cada compra.

  - Por ningún motivo se puede eliminar o editar una compra

  - La pantalla de ingreso de una compra debe solictar el cliente a través de un ComboBox, la fecha con un DatePicker. Así mismo debe permitir la selección de varios productos. El valor total de la compra se recalculará cada vez que el usuario seleccione  quite un producto. La fecha de la compra debe mostrar la fecha por defecto


  - La pantalla de detalles se mostrará de manera muy similar con la diferencia que no permitirá ninguna edición. Se recomienda el uso únicamente de Labels para el despliegue

 

## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL o SQLite

### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~

## Comandos útiles

### Iniciar servidor
#### Linux o MacOS
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación

** Nota: ** No olvidar el punto "." para que la aplicación se cree en el directorio raíz

#### Linux o MacOS
~~~
python3 manage.py startapp <nombre_de_la_aplicacion> .
~~~
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion> .
~~~

### Crear Súper Usuario
#### Linux o MacOS
~~~
python3 manage.py createsuperuser
~~~
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Linux o MacOS
~~~
python3 manage.py makemigrations
~~~
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Linux o MacOS
~~~
python3 manage.py migrate
~~~
#### Windows
~~~
python manage.py migrate
~~~

### Desplegar SQL's ejecutados en migración
#### Linux o MacOS
~~~
python3 manage.py sqlmigrate pokedex 0001
~~~
#### Windows
~~~
python manage.py sqlmigrate pokedex 0001
~~~

### Almacenar depdendencias y librerías instaladas
#### Linux o MacOS
~~~
pip3 freeze > requirements.txt
~~~
#### Windows
~~~
pip freeze > requirements.txt
~~~

# Ejemplos de Cadenas de Conexión para Django

### PostgreSQL

- Instalar pyscopg2
    ```bash
    pip3 install psycopg2
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
### MySQL
- Instalar mysqlclient
    ```bash
    pip3 install mysqlclient
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

### SQLite
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

### Oracle

- Instalar cx_Oracle
    ```bash
    pip3 install cx_Oracle
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1521',
        }
    }
    ```

### SQL Server (usando django-mssql-backend)

- Instalar cx_Oracle
    ```bash
    pip3 install django-mssql-backend
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1433',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
    ```
