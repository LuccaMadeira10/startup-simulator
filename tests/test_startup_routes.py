from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_create_startup_returns_created_startup():
    response = client.post(
        "/startups",
        json={
            "name": "Minha Startup",
            "industry": "EdTech",
            "initial_capital": 100000,
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["id"] >= 1
    assert data["name"] == "Minha Startup"
    assert data["industry"] == "EdTech"


def test_simulate_month_returns_result_and_state():
    create_response = client.post(
        "/startups",
        json={
            "name": "Simula AI",
            "industry": "SaaS",
            "initial_capital": 50000,
        },
    )
    startup_id = create_response.json()["id"]

    simulate_response = client.post(
        f"/startups/{startup_id}/simulate",
        json={
            "marketing_budget": 800,
            "product_investment": 400,
            "hiring_count": 1,
        },
    )

    assert simulate_response.status_code == 200
    data = simulate_response.json()
    assert data["startup_id"] == startup_id
    assert data["result"]["month"] == 1
    assert data["state"]["month"] == 1


def test_history_endpoint_returns_simulation_history():
    create_response = client.post(
        "/startups",
        json={
            "name": "Historico Tech",
            "industry": "FinTech",
            "initial_capital": 70000,
        },
    )
    startup_id = create_response.json()["id"]

    client.post(
        f"/startups/{startup_id}/simulate",
        json={
            "marketing_budget": 200,
            "product_investment": 200,
            "hiring_count": 0,
        },
    )

    history_response = client.get(f"/startups/{startup_id}/history")

    assert history_response.status_code == 200
    history = history_response.json()
    assert len(history) == 1
    assert history[0]["startup_id"] == startup_id
