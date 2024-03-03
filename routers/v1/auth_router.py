"""
    Módulo de los controladores de la autenticación
"""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from schemas.auth_schema import TokenSchema
from services.auth_service import AuthService



AuthRouter = APIRouter(
    prefix="/auth", tags=["Autenticación"],
    responses={404: {"description": "No encontrado"}},
)

@AuthRouter.post("/login", response_model=TokenSchema)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthService = Depends()
    ) -> TokenSchema:
    """Controlador para la autenticación de usuario.

    Args:
        form_data (Annotated[OAuth2PasswordRequestForm, Depends): 
        Modelo con todos los atributos disponibles para un flujo oauth2. 
        Solo se va autilizar los atributos username y password
        
        auth_service (AuthService, optional): Inyección del servicio auth.

    Raises:
        HTTPException: Usuario o contraseña incorrecta el sistema retorna error 401

    Returns:
        TokenSchema: Token de acceso del usuario
    """
    token = auth_service.login(form_data.username, form_data.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrecto",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token
