from app import app 

from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
   data = []
   user_data ={'nombre_user':'Jayr','edad':27,'tipo_user':'admin','correo':'jayrmz@realdental.com'}
   consult_data ={'ubicacion':'1223','nombre':'Real Dental','numero_citas':5}
   data.append(user_data)
   data.append(consult_data)
   return render_template("admin/admin_dashboard.html",data = data )

@app.route('/admin/perfil')
def admin_profile():
    return 'PERFIL USUARIO'

