"""
 Módulo que define los servicios del usuario
"""
from typing import List, Optional

from fastapi import Depends

from models.UserModel import User
from repositories.user_repository import UserRepository
from schemas.user_schema import (
    UserCreateRequestSchema,
    UserQuerySchema,
    UserSchema,
    UserUpdateRequestSchema)

class UserService:
    """
        Servicios del usuario
    """
    user_repository: UserRepository

    def __init__(
        self, user_repository: UserRepository = Depends()
    ) -> None:
        """
        Constructor de la clase UserService.

        Args:
            userRepository (UserRepository, optional): 
                Repositorio de usuarios. Defaults to Depends().
        """
        self.user_repository = user_repository

    def create(self, instance: UserCreateRequestSchema) -> UserSchema:
        """
        Crea un nuevo usuario.

        Args:
            instance (UserCreateRequestSchema): Datos del usuario a crear.

        Returns:
            UserSchema: El usuario creado.
        """
        user = User(**instance.model_dump())
        return self.user_repository.create(user)

    def list(
        self,
        query_params: Optional[UserQuerySchema],
        limit: Optional[int],
        start: Optional[int]
        ) -> List[UserSchema]:
        """
        Obtiene una lista de usuarios con filtros opcionales.

        Args:
            query_params (UserQuerySchema, optional): Parámetros de consulta. Defaults to None.
            limit (int, optional): Límite de resultados. Defaults to None.
            start (int, optional): Índice de inicio. Defaults to None.

        Returns:
            List[UserSchema]: Lista de usuarios que coinciden con los filtros.
        """
        return self.user_repository.list(query_params, limit, start)

    def get(self, user_id: int) -> User:
        """
        Obtiene un usuario por su ID.

        Args:
            user_id (int): ID del usuario.

        Returns:
            User: El usuario encontrado.
        """
        return self.user_repository.get(user_id)

    def delete(self, user_id: int) -> None:
        """
        Elimina un usuario por su ID.

        Args:
            id (int): ID del usuario a eliminar.
        """
        return self.user_repository.delete(user_id)

    def update(self, user_id: int, instance: UserUpdateRequestSchema) -> UserSchema:
        """
        Actualiza un usuario existente.

        Args:
            user_id (int): ID del usuario a actualizar.
            instance (UserUpdateRequestSchema): Datos actualizados del usuario.

        Returns:
            UserSchema: El usuario actualizado.
        """
        user = User(**instance.model_dump())
        return self.user_repository.update(user_id, user)
