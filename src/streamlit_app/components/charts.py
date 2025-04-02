import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Any, Optional, Union, Tuple


def create_line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: List[str],
    title: str = "Line Chart",
    height: int = 400,
) -> None:
    """
    Create and display a line chart using Streamlit's native chart function.
    
    Args:
        df: DataFrame containing the data
        x_col: Column name for x-axis
        y_cols: List of column names for y-axis
        title: Chart title
        height: Chart height in pixels
    """
    st.subheader(title)
    
    chart_data = df.set_index(x_col)[y_cols]
    
    st.line_chart(chart_data, height=height)


def create_bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None,
    title: str = "Bar Chart",
    orientation: str = "vertical",
) -> None:
    """
    Create and display a bar chart using Plotly.
    
    Args:
        df: DataFrame containing the data
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color_col: Column name for color grouping
        title: Chart title
        orientation: Chart orientation ('vertical' or 'horizontal')
    """
    st.subheader(title)
    
    if orientation == "horizontal":
        fig = px.bar(
            df,
            y=x_col,
            x=y_col,
            color=color_col,
            title=title,
            orientation='h',
        )
    else:
        fig = px.bar(
            df,
            x=x_col,
            y=y_col,
            color=color_col,
            title=title,
        )
    
    fig.update_layout(
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_scatter_plot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None,
    size_col: Optional[str] = None,
    title: str = "Scatter Plot",
) -> None:
    """
    Create and display a scatter plot using Plotly.
    
    Args:
        df: DataFrame containing the data
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color_col: Column name for color
        size_col: Column name for point size
        title: Chart title
    """
    st.subheader(title)
    
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        size=size_col,
        title=title,
        opacity=0.7,
    )
    
    fig.update_layout(
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_heatmap(
    df: pd.DataFrame,
    title: str = "Correlation Heatmap",
) -> None:
    """
    Create and display a correlation heatmap using Plotly.
    
    Args:
        df: DataFrame containing numeric data
        title: Chart title
    """
    st.subheader(title)
    
    corr_matrix = df.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='RdBu_r',
        zmin=-1,
        zmax=1,
    ))
    
    fig.update_layout(
        height=600,
        title=title,
    )
    
    st.plotly_chart(fig, use_container_width=True)


def create_pie_chart(
    df: pd.DataFrame,
    values_col: str,
    names_col: str,
    title: str = "Pie Chart",
) -> None:
    """
    Create and display a pie chart using Plotly.
    
    Args:
        df: DataFrame containing the data
        values_col: Column name for values
        names_col: Column name for segment names
        title: Chart title
    """
    st.subheader(title)
    
    fig = px.pie(
        df,
        values=values_col,
        names=names_col,
        title=title,
    )
    
    fig.update_layout(
        height=500,
    )
    
    st.plotly_chart(fig, use_container_width=True)
