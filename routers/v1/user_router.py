"""
    Módulo de los controladores del usuario
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from infrastrucure.decorators.role_decorator import has_permission
from infrastrucure.security.authtentication import oauth2_scheme

from schemas.user_schema import (
    UserSchema,
    UserQuerySchema,
    UserCreateRequestSchema,
    UserUpdateRequestSchema
    )
from services.user_service import UserService

UserRouter = APIRouter(
    prefix="/users", tags=["User"],
    responses={404: {"description": "No encontrado"}},
)

@UserRouter.get("/", response_model=List[UserSchema])
@has_permission('admin')
async def get_all_users(
    limit: int = Query(None, description="Limitar el número de resultados"),
    start: int = Query(None, description="Comenzar los resultados desde este índice"),
    username: str = Query(None, description="Valor de nombre de usuario"),
    email: str = Query(None, description="Valor de correo electrónico"),
    role_id: int = Query(None, description="ID del rol"),
    user_service: UserService = Depends(),
    _token: str = Depends(oauth2_scheme)
):
    """
    Obtener una lista de usuarios con filtros opcionales.

    - **limit**: Limitar el número de resultados.
    - **start**: Comenzar los resultados desde este índice.
    - **username**: Filtrar por nombre de usuario.
    - **email**: Filtrar por correo electrónico.
    - **role_id**: Filtrar por ID de rol.

    Returns:
        List[UserSchema]: Lista de usuarios que coinciden con los filtros.
    """
    query = UserQuerySchema()
    query.username = username
    query.email = email
    query.role_id = role_id
    users = user_service.list(limit=limit, start=start, query_params=query)
    return users

@UserRouter.get("/{user_id}", response_model=UserSchema)
@has_permission('admin')
async def get_user(
    user_id: int, 
    user_service: UserService = Depends(), 
    _token: str = Depends(oauth2_scheme)):
    """
    Obtener un usuario por su ID.

    Args:
        user_id (int): El ID del usuario.

    Returns:
        UserSchema: La información del usuario.
    """
    user = user_service.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@UserRouter.post("/", response_model=UserSchema)
@has_permission('admin')
async def create_user(
    user: UserCreateRequestSchema, 
    user_service: UserService = Depends(),
    _token: str = Depends(oauth2_scheme)):
    """
    Crear un nuevo usuario.

    Args:
        usuario (UserCreateRequestSchema): Los datos para crear un nuevo usuario.

    Returns:
        UserSchema: El usuario recién creado.
    """
    return user_service.create(user)

@UserRouter.patch("/{user_id}", response_model=UserSchema)
@has_permission('admin')
def update(
    user_id: int,
    user: UserUpdateRequestSchema,
    user_service: UserService = Depends(),
    _token: str = Depends(oauth2_scheme)):
    """
    Actualizar un usuario existente.

    Args:
        user_id (int): El ID del usuario a actualizar.
        usuario (UserUpdateRequestSchema): Los datos actualizados del usuario.

    Returns:
        UserSchema: La información actualizada del usuario.
    """
    user = user_service.update(user_id, user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@UserRouter.delete("/{user_id}", response_model=UserSchema)
@has_permission('admin')
def delete(
    user_id: int,
    user_service: UserService = Depends(),
    _token: str = Depends(oauth2_scheme)):
    """
    Eliminar un usuario por su ID.

    Args:
        user_id (int): El ID del usuario a eliminar.

    Returns:
        UserSchema: El usuario eliminado.
    """
    try:
        return user_service.delete(user_id)
    except Exception as exc:
        raise HTTPException(status_code=404, detail="User not found") from exc
