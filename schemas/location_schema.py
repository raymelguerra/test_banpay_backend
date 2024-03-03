"""Módulo de locación
"""
from typing import List
from pydantic import BaseModel

class LocationSchema(BaseModel):
    """
    Esquema Pydantic para la locación en el JSON proporcionado.

    Args:
        id (str): ID único de la locación.
        name (str): Nombre de la locación.
        climate (str): Clima de la locación.
        terrain (str): Terreno de la locación.
        surface_water (str): Porcentaje de agua en la superficie de la locación.
        residents (List[HttpUrl]): Lista de URLs de los residentes asociados con la locación.
        films (List[HttpUrl]): Lista de URLs de las películas asociadas con la locación.
        url (HttpUrl): URL de la locación.
    """

    id: str
    name: str
    climate: str
    terrain: str
    surface_water: str
    residents: List[str]
    films: List[str]
    url: str
