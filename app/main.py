from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.slider import router as slider_router
from app.api.v1.auth import router as auth_router
from app.api.v1.image import router as image_router

app = FastAPI(title="Shofy Catalog")

Base.metadata.create_all(bind=engine)

app.include_router(slider_router)

app.include_router(auth_router)
app.include_router(image_router)

@app.get("/")
def root():
    return {"message": "Welcome to ShofyAPI!"}
