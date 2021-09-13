from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app_python.display_time import api

from prometheus_fastapi_instrumentator import Instrumentator


def get_application():
    _app = FastAPI(title="Moscow Time")

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(api, prefix="")

    return _app


app = get_application()

Instrumentator().instrument(app).expose(app)
