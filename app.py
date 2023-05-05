from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask import Flask
app = Flask(__name__) # Se crea instancia

#Clave secreta, normalmente necesario para flask
app.secret_key = 'mysecret'
# Se asigna URL de DataBASE y se indica False a SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
print(DATABASE_CONNECTION_URI)
# Tiempo máximo de caché = 0
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#Se inicia conexión a BD
SQLAlchemy(app)
app.register_blueprint(contacts) 

