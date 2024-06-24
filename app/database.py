import os
import mysql.connector
from flask import g
from dotenv import load_dotenv

#Carga de las variables de entorno 
load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306) 
}

#Conexión a la base de Datos MySQL
def get_db():
    #Si 'db' no está previsto en el contexto global de Flask 'g'
    if 'db' not in g:
        #Crea una nueva conexión de base de datos y guardar
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    #Retornar la conexión de la base de datos
    return g.db

#Cerrar la conexión 
def close_db(e=None):
    #Extraer la conexión a la base de datos 'g' y eliminarla
    db = g.pop('db', None)
    #Si la conexión existe, cerrarla
    if db is not None:
        db.close()
        
#Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    #Registrar 'close_db' para que se ejecute al final del contexto
    app.teardown_appcontext(close_db)

