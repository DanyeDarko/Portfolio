from app import app 

from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
   dict = {'Nombre':'Daniel','Apellido':'Brito','Score':50}
   return render_template("admin/admin_dashboard.html",result = dict)

@app.route('/admin/perfil')
def admin_profile():
    return 'PERFIL USUARIO'

