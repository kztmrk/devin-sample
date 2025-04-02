import pytest
import os
from src.streamlit_app.config.config import load_config, get_config_value, update_config


def test_load_config():
    """Test the load_config function."""
    os.environ["APP_NAME"] = "Test App"
    os.environ["DEBUG"] = "true"
    
    config = load_config()
    
    assert config["app_name"] == "Test App"
    assert config["debug"] is True
    
    assert config["app_version"] == "0.1.0"
    assert config["environment"] == "development"
    
    del os.environ["APP_NAME"]
    del os.environ["DEBUG"]


def test_get_config_value():
    """Test the get_config_value function."""
    os.environ["APP_NAME"] = "Test App"
    
    value = get_config_value("app_name")
    assert value == "Test App"
    
    value = get_config_value("non_existent_key", "default_value")
    assert value == "default_value"
    
    del os.environ["APP_NAME"]


def test_update_config():
    """Test the update_config function."""
    try:
        update_config("test_key", "test_value")
        update_config("app_name", "Updated App Name")
        assert True
    except Exception as e:
        pytest.fail(f"update_config raised {type(e).__name__} unexpectedly: {e}")
