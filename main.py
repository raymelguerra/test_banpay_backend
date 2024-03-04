
"""
   Módulo principal, punto de inicio de la App
"""
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.environment import get_environment_variables
from infrastructure.middlewares.sql_alchemy_middleware import SQLAlchemyMiddleware
from metadata.tags import Tags
from metadata.initializer_seeder import seed_data
from models.BaseModel import init
from routers.v1.auth_router import AuthRouter
from routers.v1.ghibli_router import GhibliRouter
from routers.v1.user_router import UserRouter
from infrastructure.data_base import (
    get_db_connection,
)

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
app.include_router(GhibliRouter)

# Initialize Data Model Attributes
init()

#Hacer carga inicial de los datos
db = get_db_connection()
seed_data(db)
db.close()
