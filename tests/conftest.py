import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.routes.startup_routes import reset_in_memory_storage


@pytest.fixture(autouse=True)
def clean_in_memory_data():
    reset_in_memory_storage()
    yield
