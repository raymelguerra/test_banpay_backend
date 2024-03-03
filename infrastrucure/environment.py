"""
Módulo de configuración de las variables de entorno
"""
from functools import lru_cache
import os

from pydantic_settings import BaseSettings


@lru_cache
def get_env_filename():
    """
    Retorna según el entorno activo los valores de las variables de entorno asociado.
    """
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    """
    Clase que mapea las variables de entorno.
    """
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DEBUG_MODE: bool

    class Config:
        """
        Obtener el archivo de configuración de las variables de entorno y ajustar la codificación.
        """
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    """
    Devuelve los valores de las variables de entorno.
    """
    return EnvironmentSettings()
