PIZZAPIZZA WEB APP
==================
  
 *Aplicación en formato web que almacena una lista de pizzas, con las recetas de estas. Permite la visualización de los detalles de las pizzas, así como sus ingredientes y un análisis más exhaustivo de estos últimos. Además mediante el inicio de sesión o registro los distintos usuarios pueden hacer comentarios/reseñas sobre las diferentes pizzas que los demás usuarios de la aplicación podrán ver.*

  
## 1.- *Software que se necesita para instalar:*
  * [Visual Studio Code](https://code.visualstudio.com/) o cualquier otro editor de Python.
  * [Pip](https://pypi.org/project/pip/) para permitir la instalación de paquetes mediante cmd.
  * [Python](https://www.python.org/downloads/release/python-391/)==3.9.1.
  * [MongoDBCompass](https://www.mongodb.com/products/compass) para ver la Base de Datos que hemos creado.
## 2.- *Servicios que hay que arrancar:*
  * Abrir VisualStudioCode e importar el proyecto.
  * Comprobar que se ha instalado la versión exacta de python.
  * Asegurarse que se esté a la altura del fichero *mange.py*.
  * Ejecutar el comando *pip install -r requirements.txt* para instalar las dependencias.
  * No es necesaria la instalación y ejecución de un entorno virtual.
## 3.- *Dependencias que hay que instalar:*
  * **bson==0.5.8:** Sirve para intercambiar datos con mongoDB(Al instalar djongo versión 1.3.1 se instala de manera automática).
  * **Django==2.2.25:** Framework web que se utiliza.
  * **django-currentuser==0.5.3:** Instala el CurrentUserField() en los modelos.
  * **djongo==1.3.1:** Para mapear los objetos en Python a documentos mongoDB.
  * **pymongo==3.10.1:** Contiene todas las herramientas para trabajar con mongoDB.
  * Si se utiliza un macOs se deberán realizan los siguientes pasos:
     * Instalar **[homebrew](https://brew.sh/index_es):** /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     * Iniciar mongoDB:
        * **brew tap mongodb/brew**
        * **brew install mongodb-community**
        * **brew services start mongodb-community**  
   
  * **IMPORTANTE(14/01/2022): Si no se utilizan estas versiones el proyecto nos va a dar errores al conectarlo con mongoDB.**
## 4.- *Como arrancar la parte servidora:*
  * ***python manage.py makemigrations:** Nos permitire guardar los cambios que hemos hecho que tienen efectos en la Base de Datos de nuestro proyecto(Si se está en mac python3).*
  * ***python manage.py migrate:** Para que los cambios realizados en la bd guardados con el anterior comando se hagan efectivos(Si se está en mac python3).*
  * ***python manage.py runserver:** Para poner el servidor en funcionamiento y arrancar la parte backend(Si se está en mac python3).*
## 5.- *Como acceder a la parte cliente:*
  * Para acceder a la página web creada deberemos introducir la siguiente dirección en el navegador de nuestro ordenador: **http://127.0.0.1:8000/proyecto/**
  * Si queremos acceder al menú de administración debemos introducir la siguiente dirección: **http://127.0.0.1:8000/admin/** (admin; admin)

    