import os
from typing import Dict, Any, Optional
import streamlit as st


def load_config() -> Dict[str, Any]:
    """
    Load configuration from environment variables or defaults.
    
    Returns:
        Dictionary containing configuration values
    """
    config = {
        "app_name": os.environ.get("APP_NAME", "Streamlit Python Application"),
        "app_version": os.environ.get("APP_VERSION", "0.1.0"),
        "debug": os.environ.get("DEBUG", "false").lower() == "true",
        "environment": os.environ.get("APP_ENV", "development"),
        
        "data_path": os.environ.get("DATA_PATH", "data"),
        "sample_data_size": int(os.environ.get("SAMPLE_DATA_SIZE", "100")),
        
        "theme_color": os.environ.get("THEME_COLOR", "#4CAF50"),
        "sidebar_width": int(os.environ.get("SIDEBAR_WIDTH", "300")),
        "show_footer": os.environ.get("SHOW_FOOTER", "true").lower() == "true",
    }
    
    return config


def get_config_value(key: str, default: Optional[Any] = None) -> Any:
    """
    Get a specific configuration value.
    
    Args:
        key: Configuration key
        default: Default value if key is not found
        
    Returns:
        Configuration value
    """
    try:
        if "config" not in st.session_state:
            st.session_state.config = load_config()
        return st.session_state.config.get(key, default)
    except (RuntimeError, AttributeError):
        config = load_config()
        return config.get(key, default)


def update_config(key: str, value: Any) -> None:
    """
    Update a configuration value.
    
    Args:
        key: Configuration key
        value: New value
    """
    try:
        if "config" not in st.session_state:
            st.session_state.config = load_config()
        st.session_state.config[key] = value
    except (RuntimeError, AttributeError):
        pass
