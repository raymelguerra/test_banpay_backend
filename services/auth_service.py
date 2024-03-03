"""
 Módulo que define los servicios de autenticación
"""
from fastapi import Depends
from infrastrucure.security.authtentication import create_access_token, verify_password

from repositories.user_repository import UserRepository
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserQuerySchema

class AuthService:
    """
        Servicios de autenticación
    """
    user_repository: UserRepository

    def __init__(
        self, user_repository: UserRepository = Depends()
    ) -> None:
        """
        Constructor de la clase AuthService.

        Args:
            userRepository (UserRepository, optional): 
                Repositorio de usuarios. Defaults to Depends().
        """
        self.user_repository = user_repository

    def login(self, username: str, password: str) -> TokenSchema | None:
        """Devuelve el token de acceso del usuario

        Args:
            username (str): nombre de usuario
            password (str): contraseña

        Returns:
            TokenSchema: Retorna el token de acceso del usuario. 
            Si no encuentra el usuario o  falla la verificación de contraseña se retorna None
        """
        query = UserQuerySchema()
        query.username = username
        users = self.user_repository.list(query)
        if len(users) == 0:
            return None
        user = users[0]
        if not verify_password(password, user.password):
            return None
        access_token = create_access_token(data={"sub": user.username, "role": user.role.name})
        return TokenSchema(access_token=access_token, token_type="bearer")
