"""Módulo de peliculas
"""
from typing import List
from pydantic import BaseModel

class FilmSchema(BaseModel):
    """
    Esquema Pydantic para el film en el JSON proporcionado.

    Args:
        id (str): ID único del film.
        title (str): Título del film.
        original_title (str): Título original del film.
        original_title_romanised (str): Título original romanizado del film.
        description (str): Descripción del film.
        director (str): Director del film.
        producer (str): Productor del film.
        release_date (str): Año de estreno del film.
        running_time (str): Duración del film.
        rt_score (str): Puntuación de Rotten Tomatoes del film.
        people (List[HttpUrl]): Lista de URLs de las personas asociadas con el film.
        species (List[HttpUrl]): Lista de URLs de las especies asociadas con el film.
        locations (List[HttpUrl]): Lista de URLs de las locaciones asociadas con el film.
        vehicles (List[HttpUrl]): Lista de URLs de los vehículos asociados con el film.
        url (HttpUrl): URL del film.
    """

    id: str
    title: str
    original_title: str
    original_title_romanised: str
    description: str
    director: str
    producer: str
    release_date: str
    running_time: str
    rt_score: str
    people: List[str]
    species: List[str]
    locations: List[str]
    vehicles: List[str]
    url: str
