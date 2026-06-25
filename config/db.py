import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carga las variables del archivo .env que está en la raíz
load_dotenv()

def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db = os.getenv('DB_NAME')
    
    url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'
    print(f"🔌 Conectando a {db}...")
    return create_engine(url)