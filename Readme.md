Real Dental App 
=========

Simple aplicacion de gestion optima de recursos Medicos Odontologicos mediante aplicativo web con Flask/WSGI, balanceo de carga Nginx y almanecaje de Datos por postgres;Ejecutandose en una estancias de microservicios  compuestas de multiples contenedores.

Comenzando 🚀
---------------

Instala Docker [Docker Desktop](https://www.docker.com/products/docker-desktop) para distribuciones Mac o Windows. [Docker Compose](https://docs.docker.com/compose) En sistemas operativos linux ,se encuentra integrada por defecto,asegurate de ejecutar la version actual[Compose](https://docs.docker.com/compose/install/). 


## Contenedores Linux

El stack de contenedores Linux usa **Python-->Flask/WSGI**, **Nginx** , con **Redis** para messaging y **Postgres** para almacenamiento(opcionalmente **MySQL**)

> Si estas utilizando **Docker Desktop** en *Windows* [Docker Desktop on Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows), es posible correr estancias de contenedores linux ,cambiando el tipo de contenedor [switching to Linux containers](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers).

Ejecuta en el directirio raiz del proyecto:
```
docker-compose up
```
la aplicacion estara disponible con la IP del el Sistema Operativo anfitrion a traves del socket [http://localhost:8080](http://localhost:8080).


de manera alternativa , es posible levantar la aplicacion con [Docker Swarm](https://docs.docker.com/engine/swarm/), Primero,asegurate de tener instalado Swarm y ejecutandose .si no es asi,ejecuta en una *Shell*:
```
docker swarm init
```
Una ves inicialisado Docker Swarm ejecuta sobre la raiz del proyecto en una *Shell*:
```
docker stack deploy --compose-file docker-stack.yml vote
```
## ESTRUCTURA APP
```
flask
├── app/
│   ├── __init__.py
│   ├── admin_views.py
│   ├── user_views.py
│   ├── templates/
│   │   ├── admin/
│   │   │   ├── admin_templates/
│   │   │   │    └── admin_template.html
│   │   │   └── admin_dashboard.html
│   │   ├── auth/
│   │   │   └── login.html
│   │   └── public/
│   │       ├── public_templates/
│   │       │   └── user_template.html
│   │       └── user_dashboard.html  
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── app.js
├── tests/
│   └──
├── env/
├── Dockerfile
├── app.ini
├── .env
├── run.py
├── requirements.txt
└── .dockerignore
```
```
nginx
├── Dockerfile
└── nginx.conf
```
