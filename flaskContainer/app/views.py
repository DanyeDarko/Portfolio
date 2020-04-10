from app import app 
from flask import render_template

@app.route('/')
def index():
   dict = {'Nombre':'Daniel','Apellido':'Brito','Score':50}
   
   return render_template("public/index.html",result = dict)
