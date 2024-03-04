""""
Módulo de creación e interacción con la  base de datos 
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from infrastructure.environment import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()

# Generate Database URL
DATABASE_URL = (
    f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:"
    f"{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:"
    f"{env.DATABASE_PORT}/{env.DATABASE_NAME}")

# Create Database Engine
Engine = create_engine(
    DATABASE_URL, echo=env.DEBUG_MODE, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)


def get_db_connection():
    """
    Devuelve la conexión a la base de datos
    """
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
