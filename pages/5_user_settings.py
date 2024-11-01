import streamlit as st
from config import COLORS

# Initialize session state for settings if not exists
if 'user_settings' not in st.session_state:
    st.session_state.user_settings = {
        'username': '',
        'theme': 'Light',
        'notifications': False,
        'color_scheme': COLORS['primary']
    }

st.title("User Settings")

with st.sidebar:
    st.header("Settings")
    
    # User preferences form
    with st.form("settings_form"):
        username = st.text_input("Username", value=st.session_state.user_settings['username'])
        theme = st.selectbox("Theme", ["Light", "Dark", "System"], 
                           index=["Light", "Dark", "System"].index(st.session_state.user_settings['theme']))
        notifications = st.checkbox("Enable Notifications", 
                                  value=st.session_state.user_settings['notifications'])
        color_scheme = st.color_picker("Color Scheme", 
                                     value=st.session_state.user_settings['color_scheme'])
        
        if st.form_submit_button("Save Settings"):
            st.session_state.user_settings.update({
                'username': username,
                'theme': theme,
                'notifications': notifications,
                'color_scheme': color_scheme
            })
            st.success("Settings saved successfully!")

# Main content
st.subheader("Current Settings")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### User Preferences")
    st.write(f"**Username:** {st.session_state.user_settings['username']}")
    st.write(f"**Theme:** {st.session_state.user_settings['theme']}")
    st.write(f"**Notifications:** {'Enabled' if st.session_state.user_settings['notifications'] else 'Disabled'}")

with col2:
    st.markdown("### Appearance")
    st.write("**Selected Color Scheme:**")
    st.markdown(f"""
        <div style='background-color: {st.session_state.user_settings['color_scheme']}; 
                    padding: 20px; 
                    border-radius: 5px;'>
            Color Preview
        </div>
    """, unsafe_allow_html=True)

# Display data status
st.markdown("---")
st.subheader("Data Status")
if 'data' in st.session_state:
    st.success("Data is loaded")
    st.write(f"Number of rows: {len(st.session_state.data)}")
    st.write(f"Number of columns: {len(st.session_state.data.columns)}")
else:
    st.warning("No data loaded. Please upload data in the Data Upload page.")