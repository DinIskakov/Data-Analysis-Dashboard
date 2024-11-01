import streamlit as st
import pandas as pd
import numpy as np
from utils.data_operations import clean_data

st.title("Data Analysis")

if 'data' not in st.session_state:
    st.warning("Please upload data in the Data Upload page first.")
else:
    df = st.session_state['data']
    
    # Data cleaning options
    st.subheader("Data Cleaning")
    if st.button("Clean Data"):
        df = clean_data(df)
        st.session_state['data'] = df
        st.success("Data cleaned successfully!")
    
    # Summary statistics
    st.subheader("Summary Statistics")
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        st.dataframe(numeric_df.describe())
    
    # Column analysis
    st.subheader("Column Analysis")
    selected_column = st.selectbox("Select a column to analyze", df.columns)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Unique Values:", df[selected_column].nunique())
        st.write("Missing Values:", df[selected_column].isnull().sum())
        
    with col2:
        if df[selected_column].dtype in ['int64', 'float64']:
            st.write("Mean:", df[selected_column].mean())
            st.write("Median:", df[selected_column].median())
        else:
            st.write("Most Common Value:", df[selected_column].mode()[0])
            st.write("Value Counts:")
            st.dataframe(df[selected_column].value_counts().head())