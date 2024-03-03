
"""
   Módulo principal, punto de inicio de la App
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastrucure.environment import get_environment_variables
from infrastrucure.middlewares.sql_alchemy_middleware import SQLAlchemyMiddleware
from metadata.tags import Tags
from models.BaseModel import init
from routers.v1.auth_router import AuthRouter
from routers.v1.user_router import UserRouter

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
    root_path="/api/v1"
)

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SQLAlchemyMiddleware)

# Add Routers
app.include_router(UserRouter)
app.include_router(AuthRouter)


# Initialize Data Model Attributes
init()
