import pandas as pd
import numpy as np
from typing import Tuple, List

# Convert file to dataframe 
def load_data(file) -> pd.DataFrame:
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        return df
    except Exception as e:
        raise Exception(f"Error loading file: {str(e)}")

def get_basic_stats(df: pd.DataFrame) -> dict:
    stats = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': df.isnull().sum().sum(),
        'numeric_columns': len(df.select_dtypes(include=[np.number]).columns),
        'categorical_columns': len(df.select_dtypes(exclude=[np.number]).columns)
    }
    return stats

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    categorical_columns = df.select_dtypes(exclude=[np.number]).columns
    
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    
    df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
    
    return df