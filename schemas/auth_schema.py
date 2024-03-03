"""
Módulo que define los esquemas Pydantic para la autenticación.
"""
from pydantic import BaseModel


class TokenSchema(BaseModel):
    """_summary_
    """
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    """_summary_
    """
    username: str | None = None
    role: str | None = None

class LoginSchema(BaseModel):
    """
    Representa el esquema de los datos necesarios para autenticarse.
    """
    username: str
    password: str
