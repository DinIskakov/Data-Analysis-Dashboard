import streamlit as st
import pandas as pd
from utils.data_operations import load_data, get_basic_stats
from config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE

st.title("Data Upload")

# File upload
uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=ALLOWED_EXTENSIONS
)

if uploaded_file is not None:
    # Check file size
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File size is too large! Please upload a file smaller than 200MB.")
    else:
        try:
            # Load data
            df = load_data(uploaded_file)
            
            # Store in session state
            st.session_state['data'] = df
            
            # Display basic information
            st.success("File uploaded successfully!")
            
            # Basic stats
            stats = get_basic_stats(df)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Number of Rows", stats['rows'])
            with col2:
                st.metric("Number of Columns", stats['columns'])
            with col3:
                st.metric("Missing Values", stats['missing_values'])
            with col4:
                st.metric("Missing Values", stats['categorical_columns'])
                
            # Preview data
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            # Column information
            st.subheader("Column Information")
            col_info = pd.DataFrame({
                'Type': df.dtypes,
                'Non-Null Count': df.count(),
                'Null Count': df.isnull().sum()
            })
            st.dataframe(col_info)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
else:
    st.info("Please upload a file to begin analysis.")