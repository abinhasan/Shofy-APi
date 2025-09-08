from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.slider import router as slider_router

app = FastAPI(title="Shofy Catalog")

Base.metadata.create_all(bind=engine)

app.include_router(slider_router)
