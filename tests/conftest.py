import pytest
import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_dataframe():
    """
    Fixture providing a sample DataFrame for testing.
    """
    data = {
        "feature_0": [1.0, 2.0, 3.0, 4.0, 5.0],
        "feature_1": [5.0, 4.0, 3.0, 2.0, 1.0],
        "feature_2": [2.2, 3.3, 4.4, 5.5, 6.6],
        "feature_3": [0.1, 0.2, 0.3, 0.4, 0.5],
    }
    
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def sample_categorical_dataframe():
    """
    Fixture providing a sample DataFrame with categorical data for testing.
    """
    data = {
        "category": ["A", "B", "C", "A", "B"],
        "group": ["Group 1", "Group 1", "Group 2", "Group 2", "Group 3"],
        "value": [10, 20, 30, 40, 50],
    }
    
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def mock_streamlit():
    """
    Fixture for mocking Streamlit functions.
    """
    import sys
    import mock
    
    mock_st = mock.MagicMock()
    
    mock_st.subheader = mock.MagicMock()
    mock_st.line_chart = mock.MagicMock()
    mock_st.plotly_chart = mock.MagicMock()
    mock_st.sidebar = mock.MagicMock()
    mock_st.sidebar.title = mock.MagicMock()
    mock_st.sidebar.radio = mock.MagicMock()
    mock_st.set_page_config = mock.MagicMock()
    mock_st.title = mock.MagicMock()
    
    sys.modules["streamlit"] = mock_st
    
    yield mock_st
    
    if "streamlit" in sys.modules:
        del sys.modules["streamlit"]
