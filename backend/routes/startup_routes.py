from fastapi import APIRouter, HTTPException

from backend.schemas.simulation_schema import (
    RoundDecision,
    SimulationResponse,
    SimulationState,
)
from backend.schemas.startup_schema import StartupCreate, StartupResponse
from backend.services.simulation import simulate_month

router = APIRouter()

startups: dict[int, StartupResponse] = {}
startup_states: dict[int, SimulationState] = {}
startup_history: dict[int, list[SimulationResponse]] = {}

next_startup_id = 1


def reset_in_memory_storage():
    global next_startup_id

    startups.clear()
    startup_states.clear()
    startup_history.clear()
    next_startup_id = 1


@router.get("/startups")
def list_startups():
    return list(startups.values())


@router.get("/startups/{startup_id}")
def get_startup(startup_id: int):
    startup = startups.get(startup_id)
    if startup is None:
        raise HTTPException(status_code=404, detail="Startup nao encontrada")

    return {
        "startup": startup,
        "state": startup_states[startup_id],
        "history": startup_history[startup_id],
    }


@router.post("/startups", response_model=StartupResponse)
def create_startup(startup: StartupCreate):
    global next_startup_id

    startup_response = StartupResponse(
        id=next_startup_id,
        name=startup.name,
        industry=startup.industry,
        initial_capital=round(startup.initial_capital, 2),
    )

    startups[next_startup_id] = startup_response
    startup_states[next_startup_id] = SimulationState(
        month=0,
        cash=round(startup.initial_capital, 2),
        users=0,
        mrr=0,
        team_size=1,
        is_active=True,
    )
    startup_history[next_startup_id] = []

    next_startup_id += 1
    return startup_response


@router.post("/startups/{startup_id}/simulate", response_model=SimulationResponse)
def simulate_startup_month(startup_id: int, decision: RoundDecision):
    startup = startups.get(startup_id)
    if startup is None:
        raise HTTPException(status_code=404, detail="Startup nao encontrada")

    current_state = startup_states[startup_id]
    if not current_state.is_active:
        raise HTTPException(
            status_code=400,
            detail="A startup encerrou a simulacao por falta de caixa",
        )

    result, next_state = simulate_month(current_state, decision)

    response = SimulationResponse(
        startup_id=startup_id,
        decision=decision,
        result=result,
        state=next_state,
    )

    startup_states[startup_id] = next_state
    startup_history[startup_id].append(response)

    return response


@router.get("/startups/{startup_id}/history")
def get_startup_history(startup_id: int):
    if startup_id not in startups:
        raise HTTPException(status_code=404, detail="Startup nao encontrada")

    return startup_history[startup_id]
