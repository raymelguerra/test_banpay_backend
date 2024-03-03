"""
Módulo de repositorio de usuario

"""
from typing import TypeVar, List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from models.UserModel import User

from infrastrucure.data_base import (
    get_db_connection,
)

Q = TypeVar("Q")

class UserRepository():
    """
    Repositorio para la entidad User.
    """
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        """
        Constructor de la clase UserRepository.

        Args:
            db (Session, optional): Sesión de base de datos. Defaults to Depends(get_db_connection).
        """
        self.db = db

    def create(self, instance: User) -> User:
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            instance (User): Instancia del usuario a crear.

        Returns:
            User: El usuario creado.
        """
        self.db.add(instance)
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def list(
        self,
        query_params: Optional[Q],
        limit: Optional[int] | None = 100,
        start: Optional[int] | None = 0
        ) -> List[User]:
        """
        Obtiene una lista de usuarios de la base de datos con filtros opcionales.

        Args:
            query_params (Optional[Q]): Parámetros de consulta.
            limit (Optional[int]): Límite de resultados.
            start (Optional[int]): Índice de inicio.

        Returns:
            List[User]: Lista de usuarios que coinciden con los filtros.
        """
        result = self.db.query(User)
        if query_params:
            filters = {k: v for k, v in query_params.dict().items() if v is not None}
            result = result.filter_by(**filters)
        return result.offset(start).limit(limit).all()

    def get(self, user_id: int) -> User:
        """
        Obtiene un usuario por su ID de la base de datos.

        Args:
            user_id (int): ID del usuario.

        Returns:
            User: El usuario encontrado.
        """
        return self.db.get(
            User, user_id
        )

    def delete(self, user_id: int) -> None:
        """
        Elimina un usuario de la base de datos por su ID.

        Args:
            user_id (int): ID del usuario a eliminar.

        Raises:
            ValueError: Si no se encuentra un usuario con el ID especificado.
        """
        instance = self.get(user_id=user_id)
        if not instance:
            raise ValueError(f"No se encontró un usuario con el ID {id}")
        self.db.delete(instance)
        self.db.commit()
        self.db.flush()

    def update(self, user_id: int, instance: User) -> User:
        """
        Actualiza un usuario existente en la base de datos.

        Args:
            user_id (int): ID del usuario a actualizar.
            instance (User): Instancia del usuario con los datos actualizados.

        Returns:
            User: El usuario actualizado.
        """
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            return None

        for field, value in vars(instance).items():
            if value is not None:
                setattr(db_user, field, value)

        instance.id = id
        self.db.merge(instance)
        self.db.commit()
        return instance
