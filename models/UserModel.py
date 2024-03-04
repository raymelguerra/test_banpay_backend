from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta


class Role(EntityMeta):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class User(EntityMeta):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Se define la relación de uno a muchos con la tabla Role
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")
