from pydantic import BaseModel

class StartupCreate(BaseModel):
    name: str
    capital: float