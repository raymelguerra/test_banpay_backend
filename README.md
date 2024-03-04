# Prueba para Desarrollador Backend en BanPay

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Typed with: pydantic](https://img.shields.io/badge/typed%20with-pydantic-BA600F.svg?style=for-the-badge)](https://docs.pydantic.dev/)

## Descripción

Prueba para optar por el puesto de ingeniería backend para Ban Pay

Este proyecto está organizado siguiendo los principios de *Clean Architecture*, una metodología que promueve la separación clara de responsabilidades y la modularidad del código. Se ha desarrollado utilizando las siguientes tecnologías:

- [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/) **FastAPI:** Framework web de alto rendimiento para construir APIs en Python. Su enfoque en la simplicidad, rapidez y tipado estático lo hace ideal para aplicaciones modernas.
  
- [![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/) **Python 3.12:** Lenguaje de programación utilizado para toda la lógica de negocio y desarrollo de la aplicación.
  
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/) **PostgreSQL:** Base de datos relacional utilizada para almacenar los datos de la aplicación. PostgreSQL ofrece robustez, escalabilidad y un amplio conjunto de características.
  
- [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge&logo=sqlalchemy)](https://www.sqlalchemy.org/) **SQLAlchemy:** ORM (Object-Relational Mapping) utilizado para interactuar con la base de datos desde Python. Proporciona una capa de abstracción sobre las consultas SQL tradicionales.
  
- [![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/en/stable/) **Pytest:** Framework de pruebas unitarias y de integración que facilita la escritura y ejecución de pruebas en Python. Permite crear casos de prueba de manera sencilla y eficiente.
  
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/) **Docker y Docker Compose:** Herramientas utilizadas para el despliegue y la gestión de contenedores. Docker facilita la creación de entornos de desarrollo y producción consistentes y reproducibles.
  
- [![Pipenv](https://img.shields.io/badge/Pipenv-2C3E50?style=for-the-badge&logo=pipenv&logoColor=white)](https://pipenv.pypa.io/en/latest/) **Pipenv:** Gestor de paquetes utilizado para manejar las dependencias del proyecto de manera ordenada y reproducible. Proporciona un entorno virtualizado para el proyecto.
  
- [![Pylint](https://img.shields.io/badge/Pylint-1976D2?style=for-the-badge&logo=pylint&logoColor=white)](https://pylint.pycqa.org/) **Pylint:** Linter utilizado para mejorar la calidad del código. Realiza análisis estático del código Python en busca de posibles errores, convenciones de estilo y mejoras de rendimiento.


Además, el proyecto sigue las normas y principios de [![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/) para definir y documentar las APIs de manera clara y estructurada.

El proyecto se inicia con una inicialización de roles requeridos, junto con la creación de un usuario super admin por defecto. Además, se hace uso extensivo de variables de entorno para separar la configuración y mantener la seguridad de las credenciales. Las variables de entorno forma parte de este repositorio, aunque no se considera una buena práctica se procedió a incluirlas para agilizar el proceso de prueba de la app.

## Detalles del Proyecto

Este proyecto sigue la arquitectura de Clean Architecture, lo que significa que está dividido en capas independientes y con responsabilidades bien definidas. Estas capas incluyen:

- **Capa de Presentación:** Donde se encuentran las rutas de las API y las operaciones de manejo de solicitudes y respuestas.

- **Capa de Aplicación:** Responsable de la lógica de negocio y la coordinación de las operaciones entre las diferentes entidades y servicios.

- **Capa de Dominio:** Donde residen las entidades del negocio y las reglas de negocio.

- **Capa de Infraestructura:** Donde se implementan las clases concretas que interactúan con servicios externos como la base de datos y servicios de terceros.

# Instalación sin Docker

- Asegurate de tener postgres instalado y crea una base de datos con el nombre que tienes especificado en tu archivo .env


- Si lo desea puede crear un entorno virtual para esta app:

  ```sh
  $ pipenv shell
  ```

- Instalar todas las dependecias del proyecto, incluso las de desarrollo [Pipenv](https://pipenv.pypa.io):

  ```sh
  $ pipenv install --dev
  ```

- Correr la aplicación en el terminal, si no va a modificar el código, evite usar **--reload** para no recargar innecesariamente la aplicación:

  ```sh
  $ pipenv run uvicorn main:app --reload
  ```

- Abrir `localhost:8000/docs` o `localhost:8000/redoc` para la documentación de la API.

## Pruebas

- Si usted desea ejecutar prueba unitarias, como resultado obtendrá en la carpeta _**/test_report**_ el resultado de las pruebas unitarias configuradas.

  ```sh
  $ pipenv run --html=test_report/report.html
  ```

_*Nota:* Es importante volver a recargar la página, ya que se hace una limpieza de los datos para pordr ejecutar las pruebas._

  ```sh
  $ pipenv run uvicorn main:app --reload
  ```

_*Nota:* En caso de que no puedas acceder a pipenv desde las ubicaciones de tu PATH, reemplaza todas las instancias de pipenv con python3 -m pipenv._

# Instalación haciendo uso de Docker y Docker Compose

- En este archivo de *docker-compose.yml* ya tenemos además de los contenedores de la aplicación, el contenedor de postgres. Las variables de entorno configuradas para correr este docker-compose están en el fichero *prod.env*.
  
_*Note:* Para ejecutar construir los contenedores de docker se usa *pip* porque ya viene nativo en la imagen de *python:3.12-slim* usada en este proyecto, por lo que es importante verificar que exista el archivo *requirements.txt*. Si no existe este el *requirements.txt* despues de haber intalado las dependencias con pipenv y situado dentro del entorno virtual (Ver en el apartado anterior como crear el entorno virtual e instalar dependencias), ejecutar el comando:_

  ```sh
  $ pipenv requirements > requirements.txt
  ```

- Construir las imagenes de los contenedores de la app:

  ```sh
  $ docker-compose build
  ```

- Ejecutar los contenedores dentro del docker-compose

  ```sh
  $ docker-compose up -d
  ```

- Cuando obtenga los resultados de las pruebas contenidos en la carpeta _**/test_report**_, debe reiniciar el contenedor de la app, para que se cree el usuario super admin:

  ```sh
  $ docker-compose restart banpay-app
  ```

- Abrir `localhost:8000/docs` o `localhost:8000/redoc` para la documentación de la API.
