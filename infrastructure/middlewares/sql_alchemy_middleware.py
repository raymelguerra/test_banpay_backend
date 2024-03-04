"""Middleware para intersectar todas las excepciones de SQLAlchemy
"""
from fastapi import Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, NoReferencedTableError, OperationalError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_409_CONFLICT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST)


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    """ Middleware para manejar excepciones comunes de SQLAlchemy.

    Este middleware intercepta excepciones comunes de SQLAlchemy
    como IntegrityError, NoReferencedTableError y OperationalError,
    y responde con un JSON detallado.

    Args:
        BaseHTTPMiddleware: Clase base para middleware de Starlette.

    Attributes:
        No attributes.

    Methods:
        dispatch(request: Request, call_next) -> Response: Método principal del middleware
            que intercepta y maneja las excepciones.
    """
    async def dispatch(self, request: Request, call_next):
        """
        Método principal del middleware que intercepta y maneja las excepciones.

        Este método intercepta excepciones comunes de SQLAlchemy y responde
        con un JSON detallado.

        Args:
            request (Request): El objeto Request de Starlette.
            call_next: La función para llamar al siguiente middleware.

        Returns:
            JSONResponse: Una respuesta JSON con detalles del error y 
            el código de estado correspondiente.

        Raises:
            StarletteHTTPException: Se vuelve a lanzar una excepción de Starlette si ocurre.
        """
        try:
            response = await call_next(request)
            return response
        except IntegrityError as e:
            detail = "Error de integridad: " + str(e.orig)
            status_code = HTTP_409_CONFLICT
        except NoReferencedTableError:
            detail = "Error: No existe la tabla referenciada"
            status_code = HTTP_404_NOT_FOUND
        except OperationalError as e:
            detail = "Error de operación: " + str(e.orig)
            status_code = HTTP_400_BAD_REQUEST
        except StarletteHTTPException as e:
            raise e
        except (ValueError, TypeError, ResponseValidationError) as e:
            detail = "Error interno del servidor: " + str(e)
            status_code = HTTP_500_INTERNAL_SERVER_ERROR

        response_body = {"detail": detail, "status_code": status_code}
        return JSONResponse(content=response_body, status_code=status_code)
