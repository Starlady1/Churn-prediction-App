import streamlit as st
import yaml
from yaml.loader import SafeLoader
import time
import streamlit_authenticator as stauth

# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Load the configuration file
try:
    with open('./config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Configuration file 'config.yaml' not found.")
    st.stop()

# Create authenticator instance
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Handle login process
name, authentication_status, username = authenticator.login(location='sidebar')

if authentication_status:
    # User is authenticated
    authenticator.logout('Logout', location='sidebar')

    # Add CSS for animations
    st.write("""
        <style>
            @keyframes zoom-in { 0% { transform: scale(0); } 100% { transform: scale(1); } }
            @keyframes slide-in-right { 0% { transform: translateX(100%); } 100% { transform: translateX(0); } }
            @keyframes slide-in-left { 0% { transform: translateX(-100%); } 100% { transform: translateX(0); } }
            @keyframes slide-in-bottom { 0% { transform: translateY(100%); } 100% { transform: translateY(0); } }
            @keyframes slide-in-top { 0% { transform: translateY(-100%); } 100% { transform: translateY(0); } }
            .zoom-in-animation { animation: zoom-in 1.5s ease-in-out; }
            .slide-in-right-animation { animation: slide-in-right 1.5s ease-in-out; }
            .slide-in-left-animation { animation: slide-in-left 1.5s ease-in-out; }
            .slide-in-bottom-animation { animation: slide-in-bottom 1.5s ease-in-out; }
            .slide-in-top-animation { animation: slide-in-top 1.5s ease-in-out; }
        </style>
    """, unsafe_allow_html=True)

    # Display content with animations
    st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Churn Prediction App!</h1></div>', unsafe_allow_html=True)
    st.write('<div class="slide-in-bottom-animation"><h3>Unleash the power of machine learning to predict churn!</h3></div>', unsafe_allow_html=True)

    # Home Page Content
    st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="slide-in-left-animation">
            <p>Welcome to the Customer Churn Prediction Application. This tool helps businesses in the telecommunications industry 
            understand and predict customer churn. By leveraging machine learning models, it provides insights into customer behavior, 
            identifies at-risk customers, and aids in retention strategy development.</p>
        </div>
    """, unsafe_allow_html=True)

    # Split columns for Key Features and How It Works
    col1, col2 = st.columns(2)

    # Key Features
    with col1:
        st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
        st.markdown("## Key Features")
        st.markdown("""
            - **Data Exploration:** View, filter, and analyze the customer churn dataset.
            - **Account Management:** Manage your account, update details, and reset passwords.
            - **Interactive Dashboard:** Visualizations and KPIs for customer churn data analysis.
            - **Churn Prediction:** Predict churn using individual inputs or bulk data via file upload.
            - **Historical Predictions:** Review past predictions, assess trends, and evaluate model performance.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # How It Works
    with col2:
        st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
        st.markdown("## How It Works")
        st.markdown("""
            1. **Data Loading and Exploration:** Load the customer churn dataset and explore it with filtering tools.
            2. **Interactive Dashboard:** Visualize churn data, apply filters, and analyze trends.
            3. **Customer Churn Prediction:** Input customer details or upload bulk files for predictions.
            4. **Historical Predictions:** Log and review past predictions, analyze trends, and monitor performance.
            5. **Secure Authentication:** User authentication ensures secure access to the app.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer Section
    st.header("About the Developer")
    st.write("**Name:** Stella Ifeoma Fanen")
    st.write("**Background:** Junior Data Scientist")
    st.write("**Contact:** www.linkedin.com/in/stella-ifeoma-fanen/")
    st.markdown("--- © 2024 Customer Churn Prediction Project. All rights reserved.")
     
    # Need Help Section
    st.subheader("Need Help?")
    st.write("""
    - **For Collaborations:** Contact us at [sdi@azubiafrica.org](mailto:sdi@azubiafrica.org)
    """)
# Handle registration if the user is not authenticated
elif authentication_status is None:
    st.info('Please Login or Register to Proceed')

    # Registration Process
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
            location='sidebar', pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'}
        )
        
        if email_of_registered_user:
            st.success('The new user has been successfully registered.')
            time.sleep(3)

        # Save updated credentials to config file
        with open('./config.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(config, file, default_flow_style=False)

    except stauth.RegisterError as e:
        st.error(f"Error registering user: {e}")

# Incorrect login credentials
else:
    st.error('Wrong username or password')




