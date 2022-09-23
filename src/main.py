from fastapi import FastAPI
from src.routers import images

app = FastAPI()

app.include_router(images.router)


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/heartbeat")
def heartbeat():
    return "UP"
