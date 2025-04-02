import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Union, Tuple


def load_sample_data(rows: int = 100, columns: int = 5) -> pd.DataFrame:
    """
    Generate sample data for demonstration purposes.
    
    Args:
        rows: Number of rows in the dataset
        columns: Number of columns in the dataset
        
    Returns:
        DataFrame with random data
    """
    col_names = [f"feature_{i}" for i in range(columns)]
    
    data = np.random.randn(rows, columns)
    
    df = pd.DataFrame(data, columns=col_names)
    
    df.index = pd.date_range(start="2023-01-01", periods=rows, freq="D")
    
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic preprocessing on the data.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Preprocessed DataFrame
    """
    processed_df = df.copy()
    
    processed_df = processed_df.fillna(processed_df.mean())
    
    for col in processed_df.select_dtypes(include=np.number).columns:
        min_val = processed_df[col].min()
        max_val = processed_df[col].max()
        if max_val > min_val:
            processed_df[col] = (processed_df[col] - min_val) / (max_val - min_val)
    
    return processed_df


def create_summary_stats(df: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    """
    Create summary statistics for each column in the DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with summary statistics for each column
    """
    summary = {}
    
    for col in df.columns:
        col_stats = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "std": df[col].std(),
            "min": df[col].min(),
            "max": df[col].max(),
        }
        summary[col] = col_stats
    
    return summary


def split_data(
    df: pd.DataFrame, 
    test_size: float = 0.2, 
    random_state: Optional[int] = None
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data into training and testing sets.
    
    Args:
        df: Input DataFrame
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility
        
    Returns:
        Tuple of (train_df, test_df)
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    indices = np.random.permutation(len(df))
    test_count = int(len(df) * test_size)
    test_indices = indices[:test_count]
    train_indices = indices[test_count:]
    
    train_df = df.iloc[train_indices].copy()
    test_df = df.iloc[test_indices].copy()
    
    return train_df, test_df
