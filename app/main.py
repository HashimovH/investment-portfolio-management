import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import settings
from app import meta
from app.router import router as routers


app = FastAPI(
    title="Investment Portfolio API",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/public/v1/openapi.json",
    version=meta.__version__,
    debug=settings.APP_DEBUG,
)

app.include_router(routers)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
