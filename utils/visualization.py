import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_histogram(df: pd.DataFrame, column: str):
    fig = px.histogram(df, x=column, title=f'Distribution of {column}')
    return fig

def create_boxplot(df: pd.DataFrame, column: str):
    fig = px.box(df, y=column, title=f'Boxplot of {column}')
    return fig

def create_scatter(df: pd.DataFrame, x_col: str, y_col: str):
    fig = px.scatter(df, x=x_col, y=y_col, 
                    title=f'Scatter Plot: {x_col} vs {y_col}')
    return fig

def create_correlation_heatmap(df: pd.DataFrame):
    corr = df.select_dtypes(include=['float64', 'int64']).corr()
    fig = go.Figure(data=go.Heatmap(
        z=corr,
        x=corr.columns,
        y=corr.columns,
        colorscale='RdBu'))
    fig.update_layout(title='Correlation Heatmap')
    return fig