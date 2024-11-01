import streamlit as st
from utils.visualization import (
    create_histogram, create_boxplot,
    create_scatter, create_correlation_heatmap
)
import numpy as np

st.title("Data Visualization")

if 'data' not in st.session_state:
    st.warning("Please upload data in the Data Upload page first.")
else:
    df = st.session_state['data']
    
    # Visualization type selector
    viz_type = st.selectbox(
        "Select Visualization Type",
        ["Distribution Plots", "Relationship Plots", "Correlation Analysis"]
    )
    
    if viz_type == "Distribution Plots":
        # Select numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        selected_col = st.selectbox("Select Column", numeric_cols)
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(create_histogram(df, selected_col))
        with col2:
            st.plotly_chart(create_boxplot(df, selected_col))
            
    elif viz_type == "Relationship Plots":
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("Select X-axis", numeric_cols)
        with col2:
            y_col = st.selectbox("Select Y-axis", numeric_cols)
        
        st.plotly_chart(create_scatter(df, x_col, y_col))
        
    else:  # Correlation Analysis
        st.plotly_chart(create_correlation_heatmap(df))