""" Módulo de pruebas para user 
"""
# Fixtures
from typing import Generator
import asyncio
import pytest
from sqlalchemy.orm import Session
from models.UserModel import User, Role
from infrastructure.data_base import (
    get_db_connection,
)
from infrastructure.security.authtentication import get_password_hash
from repositories.user_repository import UserRepository
from schemas.user_schema import UserQuerySchema



@pytest.fixture(scope="module")
def db_session() -> Generator[Session, None, None]:
    """
    Fixture para crear una sesión de base de datos temporal para las pruebas.
    """
    db = next(get_db_connection())  # Obtener la sesión de la base de datos
    yield db
    db.close()


@pytest.fixture(scope="function")
def user_repository(db_session: Session) -> UserRepository:
    """
    Fixture para instanciar el repositorio de usuario para las pruebas.
    """
    return UserRepository(db=db_session)


def test_create_user(user_repository: UserRepository, db_session: Session):
    """
    Prueba la creación de un nuevo usuario en la base de datos.
    """
    admin_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = {
        "username": "Jane Smith",
        "email": "janesmith@example.com",
        "password": "Jane Smith",
        "role": admin_role
    }
    new_user = User(**user_data)
    new_user.password = get_password_hash(new_user.password)
    created_user = user_repository.create(new_user)
    assert created_user.id is not None

    # Limpiar después de la prueba
    db_session.delete(created_user)
    db_session.commit()


def test_get_user(user_repository: UserRepository, db_session: Session):
    """
    Prueba la obtención de un usuario por su ID.
    """
    admin_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = {
        "username": "Jane Smith",
        "email": "janesmith@example.com",
        "password": "Jane Smith",
        "role": admin_role
    }
    new_user = User(**user_data)
    new_user.password = get_password_hash(new_user.password)
    db_session.add(new_user)
    db_session.commit()

    retrieved_user = user_repository.get(new_user.id)
    assert retrieved_user is not None
    assert retrieved_user.username == new_user.username

    # Limpiar después de la prueba
    db_session.delete(new_user)
    db_session.commit()


def test_list_users(user_repository: UserRepository, db_session: Session):
    """
    Prueba la obtención de una lista de usuarios.
    """

    admin_role = db_session.query(Role).filter_by(name="admin").first()
    vehicle_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = [
        {
            "username": "Alice Worker",
            "email": "alice@example.com",
            "password": "Password",
            "role": admin_role,
        },
        {
            "username": "Bob Dylan",
            "email": "bob@example.com",
            "password": "Password",
            "role": vehicle_role
        },
    ]
    for data in user_data:
        new_user = User(**data)
        new_user.password = get_password_hash(new_user.password)
        db_session.add(new_user)
    db_session.commit()

    users = user_repository.list(query_params=None, limit=10, start=0)
    assert len(users) == 3

    # Limpiar después de la prueba
    for new_user in user_data:
        db_session.delete(new_user)
    db_session.commit()


def test_update_user(user_repository: UserRepository, db_session: Session):
    """
    Prueba la actualización de un usuario existente.
    """
    vehicle_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = {
        "username": "Bob Dylan",
        "email": "bob@example.com",
        "password": "Password",
        "role": vehicle_role
    }
    new_user = User(**user_data)
    new_user.password = get_password_hash(new_user.password)
    db_session.add(new_user)
    db_session.commit()

    updated_data = {
        "username": "Charlie Brown",
    }
    updated_user_id = new_user.id
    updated_user = asyncio.run(user_repository.update(updated_user_id, updated_data))

    assert updated_user is not None
    assert updated_user.username == "Charlie Brown"

    # Limpiar después de la prueba
    db_session.delete(updated_user)
    db_session.commit()


def test_delete_user(user_repository: UserRepository, db_session: Session):
    """
    Prueba la eliminación de un usuario.
    """
    vehicle_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = {
        "username": "david",
        "email": "david@example.com",
        "password": "Password",
        "role": vehicle_role
    }
    new_user = User(**user_data)
    new_user.password = get_password_hash(new_user.password)
    db_session.add(new_user)
    db_session.commit()

    deleted_user_id = new_user.id
    user_repository.delete(deleted_user_id)

    # Intentar obtener el usuario después de eliminarlo
    deleted_user = user_repository.get(deleted_user_id)
    assert deleted_user is None

    # Limpiar después de la prueba
    db_session.commit()


def test_list_users_with_filters(user_repository: UserRepository, db_session: Session):
    """
    Prueba la obtención de una lista de usuarios con filtros.
    """
    vehicle_role = db_session.query(Role).filter_by(name="admin").first()
    user_data = [
        {
            "username": "david",
            "email": "david@example.com",
            "password": "Password",
            "role": vehicle_role
        },
        {
            "username": "Fiona",
            "email": "fiona@example.com",
            "password": "Password",
            "role": vehicle_role
        },
    ]
    for data in user_data:
        new_user = User(**data)
        new_user.password = get_password_hash(new_user.password)
        db_session.add(new_user)
    db_session.commit()

    # Filtrar por username "David"
    query = UserQuerySchema()
    query.username = "david"
    users = user_repository.list(query_params=query, limit=10, start=0)
    assert len(users) == 1
    assert users[0].username == "david"

    # for new_user in user_data:
    db_session.delete(new_user)
    db_session.commit()
