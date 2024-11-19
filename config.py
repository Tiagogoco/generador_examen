POSTGRESQL = 'postgresql+psycopg2://postgres:123@localhost:5432/preguntas_db'

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    
    # Configuración de la URI de la base de datos
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    
    # Desactiva la función de seguimiento de modificaciones de SQLAlchemy, no la necesitas y evita advertencias
    SQLALCHEMY_TRACK_MODIFICATIONS = False
