from backend.schemas.simulation_schema import RoundDecision, SimulationState
from backend.services.simulation import simulate_month


def test_simulate_month_increases_users_and_updates_month():
    current_state = SimulationState(
        month=0,
        cash=50000,
        users=100,
        mrr=2500,
        team_size=1,
        is_active=True,
    )
    decision = RoundDecision(
        marketing_budget=800,
        product_investment=400,
        hiring_count=0,
    )

    result, next_state = simulate_month(current_state, decision)

    assert result.month == 1
    assert result.new_users > 0
    assert next_state.users == 320
    assert next_state.month == 1


def test_hiring_increases_team_size_and_costs():
    current_state = SimulationState(
        month=2,
        cash=80000,
        users=200,
        mrr=5000,
        team_size=2,
        is_active=True,
    )
    decision = RoundDecision(
        marketing_budget=0,
        product_investment=0,
        hiring_count=2,
    )

    result, next_state = simulate_month(current_state, decision)

    assert result.team_size_end == 4
    assert next_state.team_size == 4
    assert result.costs == 20000


def test_startup_becomes_inactive_when_cash_runs_out():
    current_state = SimulationState(
        month=1,
        cash=1000,
        users=0,
        mrr=0,
        team_size=5,
        is_active=True,
    )
    decision = RoundDecision(
        marketing_budget=0,
        product_investment=0,
        hiring_count=2,
    )

    result, next_state = simulate_month(current_state, decision)

    assert result.cash_end == 0
    assert result.is_active is False
    assert next_state.is_active is False
