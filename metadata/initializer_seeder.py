"""Inicializar la base de datos
"""
from fastapi import Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from models.UserModel import Role, User
from infrastructure.security.authtentication import get_password_hash
from infrastructure.data_base import (
    get_db_connection,
)


def seed_data(session: Session = Depends(get_db_connection)):
    """Inicaliza la abse de datos con los roles y un usuario admin
    """
    db = next(session)
    if is_database_empty(db):
        db.add(Role(name = "admin"))
        db.add(Role(name = "films"))
        db.add(Role(name = "people"))
        db.add(Role(name = "locations"))
        db.add(Role(name = "species"))
        db.add(Role(name = "vehicles"))
        db.commit()

        password= get_password_hash("P@ssw0rd")
        admin_role = db.query(Role).filter_by(name="admin").first()
        db.add(
            User(username="admin",
                 role_id=admin_role.id,
                 email="admin@test.com",
                 password=password))
        db.commit()

def is_database_empty(db: Session) -> bool:
    """
    Verifica si la base de datos está vacía.
    """
    role_count = db.query(func.count(Role.id)).scalar()
    user_count = db.query(func.count(User.id)).scalar()
    return (role_count + user_count) <= 6
