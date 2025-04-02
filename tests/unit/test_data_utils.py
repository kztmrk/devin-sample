import pytest
import pandas as pd
import numpy as np
from src.streamlit_app.utils.data_utils import (
    load_sample_data,
    preprocess_data,
    create_summary_stats,
    split_data,
)


def test_load_sample_data():
    """Test the load_sample_data function."""
    df = load_sample_data()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 5)
    
    rows, cols = 50, 3
    df = load_sample_data(rows=rows, columns=cols)
    assert df.shape == (rows, cols)
    
    assert isinstance(df.index, pd.DatetimeIndex)


def test_preprocess_data(sample_dataframe):
    """Test the preprocess_data function."""
    df = sample_dataframe.copy()
    df.iloc[0, 0] = np.nan
    
    processed_df = preprocess_data(df)
    
    assert not processed_df.isna().any().any()
    
    for col in processed_df.columns:
        assert processed_df[col].min() >= 0
        assert processed_df[col].max() <= 1


def test_create_summary_stats(sample_dataframe):
    """Test the create_summary_stats function."""
    stats = create_summary_stats(sample_dataframe)
    
    assert set(stats.keys()) == set(sample_dataframe.columns)
    
    required_stats = ["mean", "median", "std", "min", "max"]
    for col in stats:
        assert set(stats[col].keys()) == set(required_stats)
    
    col = sample_dataframe.columns[0]
    assert stats[col]["mean"] == sample_dataframe[col].mean()
    assert stats[col]["median"] == sample_dataframe[col].median()
    assert stats[col]["min"] == sample_dataframe[col].min()
    assert stats[col]["max"] == sample_dataframe[col].max()


def test_split_data(sample_dataframe):
    """Test the split_data function."""
    train_df, test_df = split_data(sample_dataframe)
    
    assert len(train_df) == int(len(sample_dataframe) * 0.8)
    assert len(test_df) == int(len(sample_dataframe) * 0.2)
    
    assert len(train_df) + len(test_df) == len(sample_dataframe)
    
    test_size = 0.3
    train_df, test_df = split_data(sample_dataframe, test_size=test_size)
    assert len(test_df) == int(len(sample_dataframe) * test_size)
    
    train_df1, test_df1 = split_data(sample_dataframe, random_state=42)
    train_df2, test_df2 = split_data(sample_dataframe, random_state=42)
    
    pd.testing.assert_frame_equal(train_df1, train_df2)
    pd.testing.assert_frame_equal(test_df1, test_df2)
