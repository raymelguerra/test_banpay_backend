"""
 Módulo que define los servicios para consumir el Ghibli
"""
from typing import TypeVar, List, Type
from httpx import AsyncClient, HTTPStatusError, RequestError

from infrastrucure.environment import  get_environment_variables

T = TypeVar("T")

class GhibliService:
    """
        Servicios del usuario
    """

    def __init__(self):
        """
        Constructor de la clase GhibliService.
        """
        self.env = get_environment_variables()

    async def get_info(
        self,
        model: Type[T],
        endpoint: str,
        limit: int | None = 50,
        endpoint_id: str | None = None
        ) -> List[T]:
        """Obtiene según el endpoint especificado los valores devueltos por GHIBLI

        Args:
            endpoint (str): Selecciona que endpoint consultar
            limit (int): Cantidad de registros a devolver, en caso de omitirlo el valor es 50
            endpoint_id (any | None): Identificador del tipo de endpoint

        Returns:
            List[T]: Retorna una lista de objetos segun el endpoint consultado
        """
        url = f"{self.env.GHIBLI_API}/{endpoint}"
        if endpoint_id:
            url = url + f"/{endpoint_id}"
        elif limit:
            url = url + f"?limit={limit}"
        else:
            url = url + "?limit=50"

        try:
            async with AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                data = response.json()
                if isinstance(data, list):
                    return[model(**item) for item in data]
                else:
                    return [model(**data)]

        except HTTPStatusError as e:
            # Manejar errores de status HTTP
            return {"error": f"HTTP status error: {e.response.status_code}"}
        except RequestError as e:
            # Manejar errores de solicitud
            return {"error": f"Request error: {str(e)}"}
