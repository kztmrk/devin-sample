import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from typing import List, Optional, Dict, Any, Union


def create_line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: List[str],
    title: str = "Line Chart",
    height: int = 400,
    width: Optional[int] = None,
) -> go.Figure:
    """
    Create a line chart using Plotly.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis
        y_cols: List of column names for y-axis
        title: Chart title
        height: Chart height in pixels
        width: Chart width in pixels
        
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    for col in y_cols:
        fig.add_trace(
            go.Scatter(
                x=df[x_col],
                y=df[col],
                mode="lines+markers",
                name=col,
            )
        )
    
    fig.update_layout(
        title=title,
        xaxis_title=x_col,
        yaxis_title="Value",
        height=height,
        width=width,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    
    return fig


def create_bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None,
    title: str = "Bar Chart",
    height: int = 400,
    width: Optional[int] = None,
) -> go.Figure:
    """
    Create a bar chart using Plotly.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color_col: Column name for color grouping
        title: Chart title
        height: Chart height in pixels
        width: Chart width in pixels
        
    Returns:
        Plotly figure object
    """
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        height=height,
        width=width,
        barmode="group" if color_col else None,
    )
    
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    
    return fig


def create_scatter_plot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None,
    size_col: Optional[str] = None,
    title: str = "Scatter Plot",
    height: int = 400,
    width: Optional[int] = None,
) -> go.Figure:
    """
    Create a scatter plot using Plotly.
    
    Args:
        df: Input DataFrame
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color_col: Column name for color grouping
        size_col: Column name for point size
        title: Chart title
        height: Chart height in pixels
        width: Chart width in pixels
        
    Returns:
        Plotly figure object
    """
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        size=size_col,
        title=title,
        height=height,
        width=width,
    )
    
    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title=y_col,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    
    return fig


def create_heatmap(
    df: pd.DataFrame,
    title: str = "Correlation Heatmap",
    height: int = 500,
    width: Optional[int] = None,
) -> go.Figure:
    """
    Create a correlation heatmap using Plotly.
    
    Args:
        df: Input DataFrame
        title: Chart title
        height: Chart height in pixels
        width: Chart width in pixels
        
    Returns:
        Plotly figure object
    """
    corr_matrix = df.corr()
    
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title=title,
        height=height,
        width=width,
    )
    
    fig.update_layout(
        xaxis_title="Features",
        yaxis_title="Features",
    )
    
    return fig


def create_pie_chart(
    df: pd.DataFrame,
    values_col: str,
    names_col: str,
    title: str = "Pie Chart",
    height: int = 400,
    width: Optional[int] = None,
) -> go.Figure:
    """
    Create a pie chart using Plotly.
    
    Args:
        df: Input DataFrame
        values_col: Column name for values
        names_col: Column name for category names
        title: Chart title
        height: Chart height in pixels
        width: Chart width in pixels
        
    Returns:
        Plotly figure object
    """
    fig = px.pie(
        df,
        values=values_col,
        names=names_col,
        title=title,
        height=height,
        width=width,
    )
    
    fig.update_traces(textposition="inside", textinfo="percent+label")
    
    return fig
