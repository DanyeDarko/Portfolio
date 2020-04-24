# CONSTRUCTOR DE app.py
from flask import Flask
# MICROFRAMEWORK FLASK PARA PRESENTAR API'S Y RENDERISAR TEMPLATES

app = Flask(__name__)
# NUEVA ESTANCIA DEL MODULO 'FLASK' LLAMADA 'app'

app.config.from_mapping(
        SECRET_KEY='dev',
)

from app import user_views,admin_views
# DEL MODULO 'app' (DIRECTORIO) IMPORTAMOS LAS VISTAS DEL USUARIO Y DEL ADMINISTRADOR