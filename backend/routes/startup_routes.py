from fastapi import APIRouter
from backend.schemas.startup_schema import StartupCreate

router = APIRouter()

startups = []

@router.get("/startups")
def list_startups():
    return startups

@router.post("/startups")
def create_startup(startup: StartupCreate):
    startups.append(startup)
    return {
        "message": "Startup criada com sucesso",
        "startup": startup
    }