import pytest
from pytest_dash.runner import DashRunner
from data import app  # Ensure app.py is correctly imported

@pytest.fixture
def dash_runner():
    """Fixture to run the Dash app in a test environment"""
    runner = DashRunner(app)  # ✅ Use DashRunner
    return runner

def test_header_present(dash_runner):
    dash_runner.start_server()
    header = dash_runner.find_element("#header")  # Adjust ID based on your app
    assert header is not None

def test_visualization_present(dash_runner):
    dash_runner.start_server()
    visualization = dash_runner.find_element("#visualization")  # Adjust ID
    assert visualization is not None

def test_region_picker_present(dash_runner):
    dash_runner.start_server()
    region_picker = dash_runner.find_element("#region-picker")  # Adjust ID
    assert region_picker is not None
