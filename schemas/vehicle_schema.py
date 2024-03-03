"""Módulo de vehiculos
"""
from typing import List
from pydantic import BaseModel

class VehicleSchema(BaseModel):
    """
    Esquema Pydantic para el vehículo en el JSON proporcionado.

    Args:
        id (str): ID único del vehículo.
        name (str): Nombre del vehículo.
        description (str): Descripción del vehículo.
        vehicle_class (str): Clase del vehículo.
        length (str): Longitud del vehículo.
        pilot (HttpUrl): URL de la persona que pilota el vehículo.
        films (List[HttpUrl]): Lista de URLs de las películas asociadas con el vehículo.
        url (HttpUrl): URL del vehículo.
    """

    id: str
    name: str
    description: str
    vehicle_class: str
    length: str
    pilot: str
    films: List[str]
    url: str
