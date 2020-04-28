from app import app 

from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
   return render_template("admin/admin_dashboard.html")

@app.route('/admin/perfil')
def admin_profile():
    return 'PERFIL USUARIO'

