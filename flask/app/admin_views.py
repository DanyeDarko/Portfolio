from app import app 
from flask import render_template


@app.route('/admin/dashboard')
def admin_dashboard():
   dict = {'Nombre':'Daniel','Apellido':'Brito','Score':50}
   return render_template("admin/dashboard.html",result = dict)
