"""Módulo para gestionar la seguridad en la autenticación
"""
# Runtime Environment Configuration
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from infrastructure.environment import get_environment_variables

env = get_environment_variables()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verificar si dos contraseñas

    Args:
        plain_password (str): Contraseña en texto plano
        hashed_password (str): contraseña cifrada

    Returns:
        bool: Retorna true si son iguales, false si no
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Cifrar la contrseña

    Args:
        password (str): Contrseña en texto plano

    Returns:
        str: retorna la contraseña cifrada
    """
    return pwd_context.hash(password)

def create_access_token(data: dict) -> str:
    """Crear un token de acceso a los usuarios que validen sus credenciales

    Args:
        data (dict): Valores a cifrar dentro del token
        NOTA: Si no tiene definido un tiempo de expiración se asume que va a ser de 15 minutos.

    Returns:
        str: EL token de acceso generado
    """
    to_encode = data.copy()
    expires_delta =  timedelta(minutes=env.ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Si no tiene definido un tiempo de expiración se asume que va a ser de 15 minutos
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, env.SECRET_KEY, algorithm=env.ALGORITHM)
    return encoded_jwt
