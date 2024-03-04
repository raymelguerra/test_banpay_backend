"""
Módulo que define los esquemas Pydantic para los usuarios.
"""
from typing import Optional
from enum import Enum
from pydantic import BaseModel, EmailStr

class RoleEnum(str, Enum):
    admin = "admin"
    films = "films"
    people = "people"
    locations = "locations"
    species = "species"
    vehicles = "vehicles"

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

class UserCreateRequestSchema(UserBaseSchema):
    """
    Representa el esquema de datos para la creación de un usuario.
    """
    username: str
    email: EmailStr
    password: str
    role_name:RoleEnum

class UserUpdateRequestSchema(UserBaseSchema):
    """
    Representa el esquema de datos para la actualización de un usuario.
    """
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = None
    password: Optional[str] = None
    role_name: Optional[str] = RoleEnum


class UserSchema(UserBaseSchema):
    """
    Representa el esquema de datos de un usuario.
    """
    id: int
    role: Optional[RoleSchema]
    role_id: int

class UserQuerySchema(BaseModel):
    """
    Representa el esquema de datos para la consulta de usuarios.
    """
    username: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[int] = None
