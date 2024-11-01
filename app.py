import streamlit as st
from config import APP_TITLE, APP_ICON

# Page config
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)

# Main content
st.title("Welcome to Data Analysis Dashboard")

st.markdown("""
### 🎯 About This App
This dashboard provides comprehensive data analysis capabilities including:
- Data upload and basic statistics
- Detailed data analysis and profiling
- Interactive visualizations
- Basic predictive modeling

### 📝 How to Use
1. Start by uploading your data in the **Data Upload** page
2. Explore basic statistics and data quality in the **Data Analysis** page
3. Create visualizations in the **Visualization** page
4. Try predictive modeling in the **Prediction** page

### 🔍 Features
- Support for CSV and Excel files
- Automated data cleaning
- Interactive charts and graphs
- Basic machine learning capabilities
""")

## Footer
st.markdown("---")
#st.markdown("Built with ❤️ using Streamlit")