import pytest
import sys
from pathlib import Path
import importlib.util


def test_app_imports():
    """Test that the app.py file can be imported without errors."""
    app_path = Path(__file__).parent.parent.parent / "src" / "streamlit_app" / "app.py"
    
    assert app_path.exists(), f"App file not found at {app_path}"
    
    spec = importlib.util.spec_from_file_location("app", app_path)
    app_module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(app_module)
        assert True
    except Exception as e:
        pytest.fail(f"Failed to import app.py: {e}")


def test_app_structure(mock_streamlit):
    """Test the basic structure of the Streamlit app."""
    app_path = Path(__file__).parent.parent.parent / "src" / "streamlit_app" / "app.py"
    spec = importlib.util.spec_from_file_location("app", app_path)
    app_module = importlib.util.module_from_spec(spec)
    
    spec.loader.exec_module(app_module)
    
    mock_streamlit.set_page_config.assert_called_once()
    
    mock_streamlit.title.assert_called_once()
    
    mock_streamlit.sidebar.title.assert_called_once()
    
    mock_streamlit.sidebar.radio.assert_called_once()
