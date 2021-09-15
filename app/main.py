from fastapi import FastAPI, Depends
from .config import Settings, get_settings


app = FastAPI()


@app.get("/ping")
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong !",
        "environment": settings.enviroment,
        "testing": settings.testing
    }
