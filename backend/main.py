from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

from routers import images

load_dotenv()

origins = [os.getenv("PRODUCTION_URL"), os.getenv("LOCAL_URL")]

print(origins)

app = FastAPI()
app.include_router(images.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> str:
    """root endpoint, used to test if the system is up

    Returns:
        str: healthcheck response
    """
    return "UP"
