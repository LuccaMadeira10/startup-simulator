from pydantic import BaseModel, Field


class SimulationState(BaseModel):
    month: int = Field(..., ge=0)
    cash: float = Field(..., ge=0)
    users: int = Field(..., ge=0)
    mrr: float = Field(..., ge=0)
    team_size: int = Field(..., ge=1)
    is_active: bool = True


class RoundDecision(BaseModel):
    marketing_budget: float = Field(..., ge=0)
    product_investment: float = Field(..., ge=0)
    hiring_count: int = Field(..., ge=0)


class RoundResult(BaseModel):
    month: int
    new_users: int
    total_users: int
    revenue: float
    costs: float
    net_result: float
    cash_end: float
    mrr_end: float
    team_size_end: int
    is_active: bool


class SimulationResponse(BaseModel):
    startup_id: int
    decision: RoundDecision
    result: RoundResult
    state: SimulationState
