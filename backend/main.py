from fastapi import FastAPI
from backend.routes.startup_routes import router as startup_router

app = FastAPI(
    title="Startup Simulator API",
    description="API para simular crescimento de startups",
    version="0.1.0"
)

@app.get("/")
def home():
    return {"message": "Startup Simulator API running"}

app.include_router(startup_router)