import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pandas as pd

st.title("Simple Prediction")

if 'data' not in st.session_state:
    st.warning("Please upload data in the Data Upload page first.")
else:
    df = st.session_state['data']
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    st.subheader("Linear Regression Model")
    
    # Feature selection
    st.write("Select features for prediction:")
    features = st.multiselect("Select features", numeric_cols)
    
    if features:
        # Target selection
        remaining_cols = [col for col in numeric_cols if col not in features]
        target = st.selectbox("Select target variable", remaining_cols)
        
        if target:
            # Prepare data
            X = df[features]
            y = df[target]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            if st.button("Train Model"):
                model = LinearRegression()
                model.fit(X_train, y_train)
                
                # Make predictions
                y_pred = model.predict(X_test)
                
                # Calculate metrics
                r2 = r2_score(y_test, y_pred)
                rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                
                # Display results
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("R² Score", f"{r2:.3f}")
                with col2:
                    st.metric("RMSE", f"{rmse:.3f}")
                
                # Feature importance
                st.subheader("Feature Importance")
                importance_df = pd.DataFrame({
                    'Feature': features,
                    'Coefficient': model.coef_
                })
                st.dataframe(importance_df)