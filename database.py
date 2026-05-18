from sqlmodel import SQLModel, create_engine, Session
import models  # Importamos tus tablas para que SQLModel las reconozca

# Nombre del archivo local donde se guardará todo
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# El argumento 'check_same_thread=False' es exclusivo y necesario para SQLite en FastAPI
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

def crear_base_de_datos():
    """Genera el archivo .db y crea todas las tablas si no existen"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Generador de sesiones para realizar consultas (Inyección de dependencias)"""
    with Session(engine) as session:
        yield session