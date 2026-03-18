from backend.schemas.simulation_schema import RoundDecision, RoundResult, SimulationState


BASE_NEW_USERS = 20
MARKETING_EFFICIENCY = 8
PRODUCT_EFFICIENCY = 4
BASE_TEAM_COST = 3000
HIRING_COST = 4000
ARPU = 25


def simulate_month(
    current_state: SimulationState,
    decision: RoundDecision,
) -> tuple[RoundResult, SimulationState]:
    next_month = current_state.month + 1
    next_team_size = current_state.team_size + decision.hiring_count
    marketing_users = int(decision.marketing_budget / MARKETING_EFFICIENCY)
    product_users = int(decision.product_investment / PRODUCT_EFFICIENCY)
    new_users = BASE_NEW_USERS + marketing_users + product_users
    total_users = current_state.users + new_users
    revenue = total_users * ARPU
    costs = (
        (next_team_size * BASE_TEAM_COST)
        + decision.marketing_budget
        + decision.product_investment
        + (decision.hiring_count * HIRING_COST)
    )

    net_result = revenue - costs
    cash_end = current_state.cash + net_result
    is_active = cash_end > 0

    result = RoundResult(
        month=next_month,
        new_users=new_users,
        total_users=total_users,
        revenue=round(revenue, 2),
        costs=round(costs, 2),
        net_result=round(net_result, 2),
        cash_end=round(max(cash_end, 0), 2),
        mrr_end=round(revenue, 2),
        team_size_end=next_team_size,
        is_active=is_active,
    )

    next_state = SimulationState(
        month=next_month,
        cash=round(max(cash_end, 0), 2),
        users=total_users,
        mrr=round(revenue, 2),
        team_size=next_team_size,
        is_active=is_active,
    )

    return result, next_state
