import pytest
import pandas as pd
import numpy as np
from src.streamlit_app.components.charts import (
    create_line_chart,
    create_bar_chart,
    create_scatter_plot,
    create_heatmap,
    create_pie_chart,
)


def test_chart_components_exist():
    """Test that all chart components exist and are callable."""
    assert callable(create_line_chart)
    assert callable(create_bar_chart)
    assert callable(create_scatter_plot)
    assert callable(create_heatmap)
    assert callable(create_pie_chart)


def test_create_line_chart_params(sample_dataframe):
    """Test that create_line_chart accepts the expected parameters."""
    df_with_index = sample_dataframe.copy()
    df_with_index['index'] = range(len(df_with_index))
    
    try:
        create_line_chart(
            df=df_with_index,
            x_col="index",
            y_cols=df_with_index.columns.tolist()[:2],
            title="Test Line Chart",
        )
        assert True
    except Exception as e:
        pytest.fail(f"create_line_chart raised {type(e).__name__} unexpectedly: {e}")


def test_create_bar_chart_params(sample_categorical_dataframe):
    """Test that create_bar_chart accepts the expected parameters."""
    try:
        create_bar_chart(
            df=sample_categorical_dataframe,
            x_col="category",
            y_col="value",
            color_col="group",
            title="Test Bar Chart",
        )
        assert True
    except Exception as e:
        pytest.fail(f"create_bar_chart raised {type(e).__name__} unexpectedly: {e}")


def test_create_scatter_plot_params(sample_dataframe):
    """Test that create_scatter_plot accepts the expected parameters."""
    try:
        create_scatter_plot(
            df=sample_dataframe,
            x_col=sample_dataframe.columns[0],
            y_col=sample_dataframe.columns[1],
            title="Test Scatter Plot",
        )
        assert True
    except Exception as e:
        pytest.fail(f"create_scatter_plot raised {type(e).__name__} unexpectedly: {e}")


def test_create_heatmap_params(sample_dataframe):
    """Test that create_heatmap accepts the expected parameters."""
    try:
        create_heatmap(
            df=sample_dataframe,
            title="Test Heatmap",
        )
        assert True
    except Exception as e:
        pytest.fail(f"create_heatmap raised {type(e).__name__} unexpectedly: {e}")


def test_create_pie_chart_params(sample_categorical_dataframe):
    """Test that create_pie_chart accepts the expected parameters."""
    try:
        create_pie_chart(
            df=sample_categorical_dataframe,
            values_col="value",
            names_col="category",
            title="Test Pie Chart",
        )
        assert True
    except Exception as e:
        pytest.fail(f"create_pie_chart raised {type(e).__name__} unexpectedly: {e}")
