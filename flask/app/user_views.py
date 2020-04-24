from app import app 
from flask import render_template

@app.route('/')
def index():
   user = {'Nombre':'Daniel','Apellido':'Brito','Score':50}
   return render_template("public/user_dashboard.html", result =  user)
