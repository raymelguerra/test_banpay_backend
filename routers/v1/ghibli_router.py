"""
    Módulo de los controladores del usuario
"""
from typing import List
from fastapi import APIRouter, Depends, Query
from schemas.film_schema import FilmSchema
from schemas.location_schema import LocationSchema
from schemas.people_schema import PeopleSchema
from schemas.specie_schema import SpeciesSchema
from schemas.vehicle_schema import VehicleSchema

from services.ghibli_endpoint_service import GhibliService
from infrastrucure.decorators.role_decorator import has_permission
from infrastrucure.security.authtentication import oauth2_scheme

GhibliRouter = APIRouter(
    prefix="/ghibli", tags=["Rutas de Ghibli"],
    responses={404: {"description": "No encontrado"}},
)

@GhibliRouter.get("/films")
@has_permission('films')
async def get_films(
    limit: int = Query(None, description="Limitar el número de resultados"),
    film_id: str = Query(None, description="ID de la película"),
    ghibli_service: GhibliService = Depends(),
    _token: str = Depends(oauth2_scheme)
    )-> List[FilmSchema]:
    """Obtiene los datos de las peliculas

    Args:
        limit (int, optional): Limitar el número de resultados.
        film_id (str, optional): ID de la película.
        ghibli_service (GhibliService, optional): Inyección del servicio que interactua con la API.
        _token (str, optional): _token del usuario autenticado. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    return await ghibli_service.get_info(FilmSchema, limit=limit, endpoint='films', endpoint_id=film_id)

@GhibliRouter.get("/people")
@has_permission('people')
async def get_people(
    limit: int = Query(None, description="Limitar el número de resultados"),
    people_id: str = Query(None, description="ID de la persona"),
    ghibli_service: GhibliService = Depends(),
    _token: str = Depends(oauth2_scheme)) -> List[PeopleSchema]:
    """Obtiene los datos de las personas

    Args:
        limit (int, optional): Limitar el número de resultados.
        people_id (str, optional): ID de la persona.
        ghibli_service (GhibliService, optional): Inyección del servicio que interactua con la API.
        _token (str, optional): _token del usuario autenticado. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    return await ghibli_service.get_info(PeopleSchema, limit=limit, endpoint='people', endpoint_id=people_id)

@GhibliRouter.get("/locations")
@has_permission('locations')
async def get_location(
    limit: int = Query(None, description="Limitar el número de resultados"),
    location_id: str = Query(None, description="ID de la localización"),
    ghibli_service: GhibliService = Depends(),
    _token: str = Depends(oauth2_scheme)) -> List[LocationSchema]:
    """Obtiene los datos de las localizaciones

    Args:
        limit (int, optional): Limitar el número de resultados.
        location_id (str, optional): ID de la localización.
        ghibli_service (GhibliService, optional): Inyección del servicio que interactua con la API.
        _token (str, optional): _token del usuario autenticado. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    # result: List[SpeciesSchema] =
    return await ghibli_service.get_info(LocationSchema, limit=limit, endpoint='locations', endpoint_id=location_id)

@GhibliRouter.get("/species")
@has_permission('species')
async def get_species(
    limit: int = Query(None, description="Limitar el número de resultados"),
    species_id: str = Query(None, description="ID de la especie"),
    ghibli_service: GhibliService = Depends(),
    _token: str = Depends(oauth2_scheme)
    ) -> List[SpeciesSchema]:
    """Obtiene los datos de las especies

    Args:
        limit (int, optional): Limitar el número de resultados.
        species_id (str, optional): ID de la localización.
        ghibli_service (GhibliService, optional): Inyección del servicio que interactua con la API.
        _token (str, optional): _token del usuario autenticado. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    return await ghibli_service.get_info(
        SpeciesSchema,
        limit=limit,
        endpoint='species',
        endpoint_id=species_id)

@GhibliRouter.get("/vehicles")
@has_permission('vehicles')
async def get_vehicles(
    limit: int = Query(None, description="Limitar el número de resultados"),
    vehicles_id: str = Query(None, description="ID de los vehiculos"),
    ghibli_service: GhibliService = Depends(),
    _token: str = Depends(oauth2_scheme)) -> List[VehicleSchema]:
    """Obtiene los datos de las especies

    Args:
        limit (int, optional): Limitar el número de resultados.
        vehicles_id (str, optional): ID del vehiculo.
        ghibli_service (GhibliService, optional): Inyección del servicio que interactua con la API.
        _token (str, optional): _token del usuario autenticado. Defaults to Depends(oauth2_scheme).

    Returns:
        _type_: _description_
    """
    return await ghibli_service.get_info(VehicleSchema, limit=limit, endpoint='vehicles', endpoint_id=vehicles_id)
