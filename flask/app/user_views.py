from app import app 
from flask import render_template
from dotenv import load_dotenv
import os 


@app.route('/')
def index_login():
   load_dotenv()
   OS = os.getenv('OS')  
   passw = os.getenv('PASS_SQL') 
   return render_template('auth/login.html',password=passw)

@app.route('/dashboard')
def user_dashboard():
   data = []
   user_data ={'nombre_user':'Daniel','edad':23,'tipo_user':'px'}
   data.append(user_data)
   return render_template('public/user_dashboard.html', data =  data)


