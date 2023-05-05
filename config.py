from dotenv import load_dotenv
import os

#carga variables de entorno del archivo .env en el sistema de archivos del proyecto.
load_dotenv()

user = os.environ["USER"]  #Estos valores entrecomillados son las variables de .env
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
database = os.environ["DATABASE"]
server = os.environ["SERVER"]
#Esta es la URL que se usará para conectarnos a la BD
DATABASE_CONNECTION_URI = f'{server}://{user}:{password}@{host}/{database}'