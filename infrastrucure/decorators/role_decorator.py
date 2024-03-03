"""Decorador para verificar el rol del usuario
"""
from functools import wraps
from fastapi import HTTPException, status
from jose import jwt, JWTError

from infrastrucure.environment import get_environment_variables

def has_permission(role_name: str):
    """
    Decorador para verificar el rol de un usuario contenido en el token.
    Args:
        allowed_roles (List[str]): Lista de roles permitidos.
    Returns:
        callable: La función del decorador.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            token = kwargs.get("token")
            if not token:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="No existe el token o es inválido"
                )

            try:
                # Decodifica el token JWT
                env = get_environment_variables()
                payload = jwt.decode(token, env.SECRET_KEY, algorithms=[env.ALGORITHM])
                # Verifica si el rol del usuario está en la lista de roles permitidos
                if payload["role"] != role_name:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Permisos insuficientes"
                    )

                # Llama a la función original
                return await func(*args, **kwargs)

            except JWTError as exc:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token de acceso inválido"
                )   from exc
        return wrapper

    return decorator
