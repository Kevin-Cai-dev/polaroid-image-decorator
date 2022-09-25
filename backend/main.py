from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import images

app = FastAPI()
app.include_router(images.router)

origins = ["http://localhost:3000", "https://localhost:3000"]

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
