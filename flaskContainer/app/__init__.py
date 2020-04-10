# constructor de la aplicacion 

from flask import Flask
# MICROFRAMEWORK FLASK PARA PRESENTAR API'S Y RENDERISAR TEMPLATES
app = Flask(__name__)
# NUEVA ESTANCIA DEL MODULO 'FLASK' LLAMADA 'app'

from app import views,admin_views
# DEL MODULO 'app' (DIRECTORIO) IMPORTAMOS LAS VISTAS 