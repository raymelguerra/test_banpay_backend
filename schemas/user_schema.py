"""
Módulo que define los esquemas Pydantic para los usuarios.
"""
from typing import Optional
from pydantic import BaseModel


class RoleSchema(BaseModel):
    """
    Representa el esquema de datos de un rol.
    """
    id: int
    name: str

class UserBaseSchema(BaseModel):
    """
    Representa los datos básicos del usuario.
    """
    username: str
    email: str
    role_id: int

class UserCreateRequestSchema(UserBaseSchema):
    """
    Representa el esquema de datos para la creación de un usuario.
    """
    username: str
    email: str
    password: str
    role_id: int

class UserUpdateRequestSchema(UserBaseSchema):
    """
    Representa el esquema de datos para la actualización de un usuario.
    """
    username: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None
    password: Optional[str] = None


class UserSchema(UserBaseSchema):
    """
    Representa el esquema de datos de un usuario.
    """
    id: int
    role: Optional[RoleSchema]

class UserQuerySchema(BaseModel):
    """
    Representa el esquema de datos para la consulta de usuarios.
    """
    username: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None
