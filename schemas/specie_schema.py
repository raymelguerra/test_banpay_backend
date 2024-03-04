""" Módulo de species
"""
from typing import List, Optional
from pydantic import BaseModel

class SpeciesSchema(BaseModel):
    """
    Esquema Pydantic para la especie en el JSON proporcionado.

    Args:
        id (str): ID único de la especie.
        name (str): Nombre de la especie.
        classification (str): Clasificación de la especie.
        eye_colors (str): Colores de los ojos de la especie.
        hair_colors (str): Colores del cabello de la especie.
        url (HttpUrl): URL de la especie.
        people (List[HttpUrl]): Lista de URLs de las personas asociadas con la especie.
        films (List[HttpUrl]): Lista de URLs de las películas asociadas con la especie.
    """
    id: Optional[str]
    name: Optional[str]
    classification: Optional[str]
    eye_colors: Optional[str]
    hair_colors: Optional[str]
    url: Optional[str]
    people: Optional[List[str]]
    films: Optional[List[str]]
