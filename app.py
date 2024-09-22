import streamlit as st
import yaml
from yaml.loader import SafeLoader
import time
import streamlit_authenticator as stauth

# Function to load the YAML configuration file
def load_app_config(config_path: str):
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.load(file, Loader=SafeLoader)
        return config
    except FileNotFoundError:
        st.error("Configuration file 'config.yaml' not found.")
        st.stop()
    except yaml.YAMLError as e:
        st.error(f"Error loading YAML file: {e}")
        st.stop()

# Function to initialize the Streamlit Authenticator
def setup_authenticator(config):
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    return authenticator

# Function to display login and registration widgets
def display_login_and_register(authenticator):
     # Set the path to your image
    image_path = "churn_image.png"  # Change this if your image is in a different location
    pg_image = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{st.image(image_path, use_column_width=True, output_format='png')}");
            background-size: contain;
            background-position: center;
            height: 100vh;
        }}
        </style>
    '''
    
    st.markdown(pg_image, unsafe_allow_html=True)
    # Toggle for login/register
    # if st.sidebar.button("Login/Register"):
    name, authentication_status, username = authenticator.login(location='sidebar')
    
    if authentication_status:
        authenticator.logout('Logout', location='sidebar')
        return True
    elif authentication_status is None:
        st.info('Please login or register to proceed.')
        email, username, name = authenticator.register_user(location='sidebar', pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'})
        if email:
            st.success('User successfully registered.')
            time.sleep(3)
            # Update the config with new credentials after registration
            with open('./config.yaml', 'w', encoding='utf-8') as file:
                yaml.dump(config, file, default_flow_style=False)
        return False
    else:
        st.error('Invalid username or password.')
        return False
    
# Home page with clickable sections
def home_page():
    st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Churn Prediction App!</h1></div>', unsafe_allow_html=True)
    st.write('<div class="slide-in-bottom-animation"><h3>Unleash the power of machine learning to predict churn!</h3></div>', unsafe_allow_html=True)

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

    # Home Page Content
    if st.button("Click to View Details"):
        st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="slide-in-left-animation">
                <p>This tool helps businesses in the telecommunications industry 
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
                - **Data Exploration:** The Data page allows users to explore the customer churn dataset. Users can view detailed descriptions of each column, filter data based on specific criteria, and get a comprehensive understanding of the dataset's structure.
                - **Interactive Dashboard:** The Dashboard page offers a variety of visualizations and key performance indicators (KPIs) to help users analyze customer churn data. The interactive charts and graphs enable users to uncover trends and patterns that influence customer churn.
                - **Customer Churn Prediction:** On the Predict page, users can input customer details to predict the likelihood of churn. The page supports both individual predictions and bulk predictions via CSV or Excel file uploads. Users can select from multiple pre-trained machine learning models to generate predictions.
                - **Prediction Models:** Use models to predict churn likelihood for individual or bulk records.
                - **Historical Predictions:** The History page provides a log of all past predictions. This feature allows users to review previous predictions, analyze trends over time, and assess the performance of different predictive models.     
        """)
           
            st.markdown('</div>', unsafe_allow_html=True)

        # How It Works
        with col2:
            st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
            st.markdown("## How It Works")
            st.markdown("""
                1. **Data Loading and Exploration:**
                    - `Data Page:` Loading the Dataset: Loads the customer churn dataset (CSV) into a Pandas DataFrame.
                    - `Exploration Tools:` Users can explore the dataset, view column descriptions, and filter data by type (numeric or categorical).
        
                2. **Interactive Dashboard:**
                    - `Visual Insights:` Provides visualizations to analyze customer churn data, showing KPIs and trends.
                    - `Filters and Customization:` Users can apply filters (e.g., Gender, Payment Method) to customize visualizations for deeper analysis.
        
                3. **Customer Churn Prediction:**
                    - `User Input:` Users input customer details like demographics and billing info.
                    - `Model Selection:` Loads pre-trained models (e.g., Logistic Regression, AdaBoost) for prediction.
                    - `Prediction:` Predicts churn likelihood and probability based on user input.
                    - `Bulk Prediction:` Allows batch processing by uploading CSV/Excel files with multiple customer records.
        
                4. **Historical Predictions:**
                    - `Record Keeping:` Logs all past predictions, including customer attributes, outcomes, probabilities, models used, and prediction times.
                    - `Analysis and Insights:` Users can review historical data to identify patterns and validate model consistency
        
                5. **Authentication and User Management:**
                    - `Secure Access:` Ensures only authenticated users can access sensitive data and tools.
                    - `Session Management:` Manages user sessions for a seamless and secure experience.
                """)
            st.markdown('</div>', unsafe_allow_html=True)
    # Footer Section
    st.subheader("About the Developer")
    st.write("**Name:** Stella Ifeoma Fanen")
    st.write("**Background:** Junior Data Scientist")
    st.write("**Contact:** [LinkedIn](https://www.linkedin.com/in/stella-ifeoma-fanen/)")
    st.markdown("--- © 2024 Customer Churn Prediction Project. All rights reserved.")

    # Need Help Section
    st.subheader("Need Help?")
    st.write("""
    - **For Collaborations:** Contact us at [sdi@azubiafrica.org](mailto:sdi@azubiafrica.org)
    """)

# Data page
def data_page():
    st.header("Data Exploration")
    st.write("This is the Data page where you can explore the customer churn dataset.")
    # Add your data exploration functionality here

# Dashboard page
def dashboard_page():
    st.header("Interactive Dashboard")
    st.write("This is the Dashboard page with visualizations and KPIs for customer churn.")
    # Add your dashboard functionality here

# Predictions page
def predictions_page():
    st.header("Customer Churn Predictions")
    st.write("This is the Predictions page where you can predict customer churn.")
    # Add your prediction functionality here

# History page
def history_page():
    st.header("Prediction History")
    st.write("This is the History page where you can view past predictions.")
    # Add your history functionality here


# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Load configuration
config = load_app_config('./config.yaml')

# Set up authenticator
authenticator = setup_authenticator(config)

# Run the app with sidebar navigation
if display_login_and_register(authenticator):
    # Add sidebar navigation
    st.sidebar.title("Navigation")
    # Welcome message
    st.sidebar.markdown(f"### Welcome, {st.session_state['username']}!")
    pages = {
        "🏡 Home": home_page,
        "📊 Data": data_page,
        "📈 Dashboard": dashboard_page,
        "🔮 Predictions": predictions_page,
        "🕰️ History": history_page
    }
    
    # Sidebar selectbox for navigation
    selected_page = st.sidebar.selectbox("Go to", options=list(pages.keys()))
    
    # Call the selected page function
    pages[selected_page]()



