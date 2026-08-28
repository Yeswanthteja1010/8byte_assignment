import logging

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.config import get_settings
from app.logging_config import configure_logging


configure_logging()

logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Production-style FastAPI application for DevSecOps demonstration",
)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": "Welcome to OctaByte Assignment",
        "environment": settings.environment,
    }


@app.get("/health/live", tags=["Health"])
def liveness():
    return {
        "status": "alive"
    }


@app.get("/health/ready", tags=["Health"])
def readiness():
    return {
        "status": "ready"
    }


Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False,
)