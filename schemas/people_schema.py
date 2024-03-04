"""Módulo de personas
"""
from typing import List
from pydantic import BaseModel

class PeopleSchema(BaseModel):
    """
    Esquema Pydantic para la persona en el JSON proporcionado.

    Args:
        id (str): ID único de la persona.
        name (str): Nombre de la persona.
        gender (str): Género de la persona.
        age (str): Edad de la persona.
        eye_color (str): Color de ojos de la persona.
        hair_color (str): Color de cabello de la persona.
        films (List[HttpUrl]): Lista de URLs de las películas asociadas con la persona.
        species (HttpUrl): URL de la especie a la que pertenece la persona.
        url (HttpUrl): URL de la persona.
    """

    id: str
    name: str
    gender: str
    age: str
    eye_color: str
    hair_color: str
    films: List[str]
    species: str
    url: str
