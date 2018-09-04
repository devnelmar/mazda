# Mazda

## liftit test

La aplicación Mazda permite registrar usuarios y vehículos, los cuales a su vez se encuentran relacionados
permitiéndole al sistema realizar búsquedas ya sea por alguno de los datos del usuario, o por datos del vehículo,
además en la vista de editar usuarios se puede acceder y ver cuántos vehículos tiene asociado el propietario,
pudiendo ver datos del vehículo como la placa, el modelo o el tipo de vehículo, sumado a lo anterior la aplicación
cuenta con un sistema de login que permite verificar que los usuarios sean los únicos que tengan acceso a las vistas que ofrece la aplicación.

Crear un entorno virtual con Python 3 e instalar los requerimientos

> pip install -r requirements 

Configuración de la base de datos:

En settings.py organizar o definir la configuracion de la base de datos en la variable DATABASES. 


Correr migraciones:

> python manage.py migrate

Para crear un usuario ejecutar el siguiente script:

> python manage.py createsuperuser

Levantar el servidor:

> python manage.py runserver

Go to: http://localhost:8000/
