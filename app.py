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
    st.write("**Name:** Fanen Stella")
    st.write("**Background:** Expert in data science, machine learning, and software development.")
    st.write("**Contact:** [LinkedIn](https://www.linkedin.com/in/tamminga-givondo/)")
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




# import streamlit as st
# import yaml
# from yaml.loader import SafeLoader
# import time
# import streamlit_authenticator as stauth

# # Function to load the YAML configuration file
# def load_app_config(config_path: str):
#     try:
#         with open(config_path, 'r', encoding='utf-8') as file:
#             config = yaml.load(file, Loader=SafeLoader)
#         return config
#     except FileNotFoundError:
#         st.error("Configuration file 'config.yaml' not found.")
#         st.stop()
#     except yaml.YAMLError as e:
#         st.error(f"Error loading YAML file: {e}")
#         st.stop()

# # Function to initialize the Streamlit Authenticator
# def setup_authenticator(config):
#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#         config['preauthorized']
#     )
#     return authenticator

# # Function to display login and registration widgets
# def display_login_and_register(authenticator):
#     name, authentication_status, username = authenticator.login(location='sidebar')
    
#     if authentication_status:
#         authenticator.logout('Logout', location='sidebar')
#         return True
#     elif authentication_status is None:
#         st.info('Please login or register to proceed.')
#         email, username, name = authenticator.register_user(location='sidebar', pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'})
#         if email:
#             st.success('User successfully registered.')
#             time.sleep(3)
#         # Update the config with new credentials after registration
#             with open('./config.yaml', 'w', encoding='utf-8') as file:
#                 yaml.dump(config, file, default_flow_style=False)
#         return False
#     else:
#         st.error('Invalid username or password.')
#         return False

# # Home page with clickable sections
# def home_page():
#     st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Customer Churn Prediction App!</h1></div>', unsafe_allow_html=True)
#     st.write('<div class="slide-in-bottom-animation"><h3>Leverage machine learning to predict customer churn!</h3></div>', unsafe_allow_html=True)

#     # Add CSS for animations
#     st.write("""
#         <style>
#             @keyframes zoom-in { 0% { transform: scale(0); } 100% { transform: scale(1); } }
#             @keyframes slide-in-right { 0% { transform: translateX(100%); } 100% { transform: translateX(0); } }
#             @keyframes slide-in-left { 0% { transform: translateX(-100%); } 100% { transform: translateX(0); } }
#             @keyframes slide-in-bottom { 0% { transform: translateY(100%); } 100% { transform: translateY(0); } }
#             @keyframes slide-in-top { 0% { transform: translateY(-100%); } 100% { transform: translateY(0); } }
#             .zoom-in-animation { animation: zoom-in 1.5s ease-in-out; }
#             .slide-in-right-animation { animation: slide-in-right 1.5s ease-in-out; }
#             .slide-in-left-animation { animation: slide-in-left 1.5s ease-in-out; }
#             .slide-in-bottom-animation { animation: slide-in-bottom 1.5s ease-in-out; }
#             .slide-in-top-animation { animation: slide-in-top 1.5s ease-in-out; }
#         </style>
#     """, unsafe_allow_html=True)

#     # Home Page Content
#     if st.button("Click to View Details"):
#         st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
#         st.markdown("""
#             <div class="slide-in-left-animation">
#                 <p>This tool is designed to help businesses understand and predict customer churn. By leveraging advanced machine learning models, it provides insights into customer behavior, identifies at-risk customers, and helps develop retention strategies.</p>
#             </div>
#         """, unsafe_allow_html=True)

#         # Split columns for Key Features and How It Works
#         col1, col2 = st.columns(2)

#         # Key Features
#         with col1:
#             st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
#             st.markdown("## Key Features")
#             st.markdown("""
#                 - **Data Exploration:** Explore the dataset with detailed descriptions and filters.
#                 - **Account Management:** Manage account settings and details.
#                 - **Interactive Dashboard:** Analyze churn data with interactive visualizations.
#                 - **Prediction Models:** Use models to predict churn likelihood for individual or bulk records.
#                 - **History:** Review past predictions and trends over time.
#             """)
#             st.markdown('</div>', unsafe_allow_html=True)

#         # How It Works
#         with col2:
#             st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
#             st.markdown("## How It Works")
#             st.markdown("""
#                 1. **Data Loading:** Load and explore the customer churn dataset.
#                 2. **Interactive Dashboard:** Visualize churn data and apply filters.
#                 3. **Churn Prediction:** Input customer details or upload bulk data for predictions.
#                 4. **History:** Log and review all past predictions.
#                 5. **Authentication:** Secure login ensures access to sensitive data.
#             """)
#             st.markdown('</div>', unsafe_allow_html=True)

# # Set page configuration
# st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# # Load configuration
# config = load_app_config('./config.yaml')

# # Set up authenticator
# authenticator = setup_authenticator(config)

# # Run the home page
# if display_login_and_register(authenticator):
#     home_page()





# import yaml
# import streamlit as st
# import streamlit_authenticator as stauth
# from yaml.loader import SafeLoader
# from streamlit_authenticator.utilities import LoginError
# import time

# # Function to load the YAML configuration file
# def load_app_config(config_path: str):
#     try:
#         with open(config_path, 'r', encoding='utf-8') as file:
#             config = yaml.load(file, Loader=SafeLoader)
#         return config
#     except FileNotFoundError:
#         st.error("Configuration file 'config.yaml' not found.")
#         st.stop()
#     except yaml.YAMLError as e:
#         st.error(f"Error loading YAML file: {e}")
#         st.stop()

# # Function to initialize the Streamlit Authenticator
# def setup_authenticator(config):
#     if 'authenticator' not in st.session_state:
#         st.session_state['authenticator'] = stauth.Authenticate(
#             config['credentials'],
#             config['cookie']['name'],
#             config['cookie']['key'],
#             config['cookie']['expiry_days'],
#             config['preauthorized']
#         )
#     return st.session_state['authenticator']

# # Function to handle login and registration
# def handle_authentication():
#     config = load_app_config('./config.yaml')
#     authenticator = setup_authenticator(config)

#     # Display login widget
#     name, authentication_status, username = authenticator.login('Login', location='sidebar')

#     # Display registration widget if not authenticated
#     if not authentication_status:
#         st.sidebar.write("---")
#         st.sidebar.header("Register")
#         try:
#             email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
#                 pre_authorization=False, 
#                 fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'}
#             )

#             if email_of_registered_user:
#                 st.sidebar.success('The new user has been successfully registered.')
#                 time.sleep(2)
#                 # Update the config with new credentials after registration
#                 with open('./config.yaml', 'w', encoding='utf-8') as file:
#                     yaml.dump(config, file, default_flow_style=False)
#         except stauth.RegisterError as e:
#             st.sidebar.error(f"Error registering user: {e}")

#     # Handle authentication status messages
#     if authentication_status:
#         authenticator.logout('Logout', location='sidebar')
#         st.sidebar.success(f"Welcome, {name}!")
#     elif authentication_status is False:
#         st.sidebar.error('Username/password is incorrect')
#     elif authentication_status is None:
#         st.sidebar.warning('Please enter your username and password')

#     return authentication_status

# # Function to display the home page (public)
# def display_home_page():
#     # Add CSS for animations
#     st.markdown("""
#         <style>
#             @keyframes zoom-in { 
#                 0% { transform: scale(0); } 
#                 100% { transform: scale(1); } 
#             }
#             @keyframes slide-in-right { 
#                 0% { transform: translateX(100%); } 
#                 100% { transform: translateX(0); } 
#             }
#             @keyframes slide-in-left { 
#                 0% { transform: translateX(-100%); } 
#                 100% { transform: translateX(0); } 
#             }
#             @keyframes slide-in-bottom { 
#                 0% { transform: translateY(100%); } 
#                 100% { transform: translateY(0); } 
#             }
#             @keyframes slide-in-top { 
#                 0% { transform: translateY(-100%); } 
#                 100% { transform: translateY(0); } 
#             }
#             .zoom-in-animation { animation: zoom-in 1.5s ease-in-out; }
#             .slide-in-right-animation { animation: slide-in-right 1.5s ease-in-out; }
#             .slide-in-left-animation { animation: slide-in-left 1.5s ease-in-out; }
#             .slide-in-bottom-animation { animation: slide-in-bottom 1.5s ease-in-out; }
#             .slide-in-top-animation { animation: slide-in-top 1.5s ease-in-out; }
#         </style>
#     """, unsafe_allow_html=True)

#     # Header with animation
#     st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Churn Prediction App!</h1></div>', unsafe_allow_html=True)
#     st.write('<div class="slide-in-bottom-animation"><h3>Unleash the power of machine learning to predict churn!</h3></div>', unsafe_allow_html=True)

#     # About the app
#     st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
#     st.markdown("""
#         <div class="slide-in-left-animation">
#             <p>Welcome to the Customer Churn Prediction Application. This tool helps businesses in the telecommunications industry 
#             understand and predict customer churn. By leveraging machine learning models, it provides insights into customer behavior, 
#             identifies at-risk customers, and aids in retention strategy development.</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # Split columns for Key Features and How It Works
#     col1, col2 = st.columns(2)

#     # Key Features
#     with col1:
#         st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
#         st.markdown("## Key Features")
#         st.markdown("""
#             - **Data Exploration:** View, filter, and analyze the customer churn dataset.
#             - **Account Management:** Manage your account, update details, and reset passwords.
#             - **Interactive Dashboard:** Visualizations and KPIs for customer churn data analysis.
#             - **Churn Prediction:** Predict churn using individual inputs or bulk data via file upload.
#             - **Historical Predictions:** Review past predictions, assess trends, and evaluate model performance.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

#     # How It Works
#     with col2:
#         st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
#         st.markdown("## How It Works")
#         st.markdown("""
#             1. **Data Loading and Exploration:** Load the customer churn dataset and explore it with filtering tools.
#             2. **Interactive Dashboard:** Visualize churn data, apply filters, and analyze trends.
#             3. **Customer Churn Prediction:** Input customer details or upload bulk files for predictions.
#             4. **Historical Predictions:** Log and review past predictions, analyze trends, and monitor performance.
#             5. **Secure Authentication:** User authentication ensures secure access to the app.
#         """)
#         st.markdown('</div>', unsafe_allow_html=True)

#     # Clickable sections to view details using Expanders
#     st.markdown("## More Details")
#     with st.expander("About the App"):
#         st.write("""
#             This app leverages machine learning to predict customer churn in the telecommunications industry. By analyzing customer data, the app identifies patterns and trends that indicate potential churn, enabling businesses to implement targeted retention strategies.
#         """)

#     with st.expander("Key Features"):
#         st.write("""
#             - **Data Exploration:** Dive deep into the customer data to understand various attributes and metrics.
#             - **Interactive Dashboard:** Gain insights through interactive charts and graphs.
#             - **Predictive Modeling:** Use advanced ML models to forecast customer churn.
#             - **Historical Analysis:** Track and analyze past predictions to refine models and strategies.
#         """)

#     # Footer Section
#     st.header("About the Developer")
#     st.write("**Name:** Fanen Stella")
#     st.write("**Background:** Expert in data science, machine learning, and software development.")
#     st.write("**Contact:** [LinkedIn](https://www.linkedin.com/in/tamminga-givondo/)")
#     st.markdown("--- © 2024 Customer Churn Prediction Project. All rights reserved.")

#     # Need Help Section
#     st.subheader("Need Help?")
#     st.write("""
#         - **For Collaborations:** Contact us at [sdi@azubiafrica.org](mailto:sdi@azubiafrica.org)
#     """)

# # Function to render the page content based on navigation
# def display_protected_page(page):
#     pages = {
#        "🏡 Home": "01_Home.py",
#        "📊 Data": "02_Data.py",
#        "📈 Dashboard": "03_Dashboard.py",
#        "🔮 Predictions": "04_Predict.py",
#        "🕰️ History": "05_History.py",
#     }

#     # Dynamically load the selected page content
#     if page in pages:
#         st.markdown(f"## {page}")
#         exec(open(pages[page]).read())

# # Main app logic
# def run_app():
#     # Set page configuration
#     st.set_page_config(page_title="Churn Prediction App", layout="wide", initial_sidebar_state="expanded")

#     # Display the public home page
#     display_home_page()

#     # Handle authentication
#     authentication_status = handle_authentication()

#     # If authenticated, show navigation to protected pages
#     if authentication_status:
#         # Define the protected pages for navigation
#         protected_pages = [
#             "📊 Data",
#             "📈 Dashboard",
#             "🕰️ History",
#             "🔮 Predictions"
#         ]

#         # Sidebar for navigation
#         selected_page = st.sidebar.radio("Navigate to", ["🏡 Home"] + protected_pages, index=0)

#         # If 'Home' is selected, display the home page
#         if selected_page == "🏡 Home":
#             display_home_page()
#         else:
#             display_protected_page(selected_page)

# if __name__ == "__main__":
#     run_app()




# import yaml
# import streamlit as st
# import streamlit_authenticator as stauth
# from yaml.loader import SafeLoader
# from streamlit_authenticator.utilities import LoginError
# import time

# # Function to load the YAML configuration file
# def load_app_config(config_path: str):
#     try:
#         with open(config_path, 'r', encoding='utf-8') as file:
#             config = yaml.load(file, Loader=SafeLoader)
#         return config
#     except FileNotFoundError:
#         st.error("Configuration file 'config.yaml' not found.")
#         st.stop()
#     except yaml.YAMLError as e:
#         st.error(f"Error loading YAML file: {e}")
#         st.stop()

# # Function to initialize the Streamlit Authenticator
# def setup_authenticator(config):
#     if 'authenticator' not in st.session_state:
#         st.session_state['authenticator'] = stauth.Authenticate(
#             config['credentials'],
#             config['cookie']['name'],
#             config['cookie']['key'],
#             config['cookie']['expiry_days'],
#             config['preauthorized']
#         )
#     return st.session_state['authenticator']

# # Function to display the login widget and handle authentication
# def display_login_and_register():
#     # Load the configuration and initialize the authenticator
#     config = load_app_config('./config.yaml')
#     authenticator = setup_authenticator(config)

#     # Display the login form if the user is not authenticated
#     if not st.session_state.get("authentication_status"):
#         st.title("🔐 Welcome to the Churn Prediction App")
#         st.write("Please log in or register to continue.")
        
#         left_column, right_column = st.columns(2)
#         with left_column:
#             st.header("Login")
#             try:
#                 name, authentication_status, username = authenticator.login(location='main')
#             except LoginError as e:
#                 st.error(e)
        
#         with right_column:
#             st.header("Register")
#             try:
#                 email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
#                     location='main', pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'}
#                 )

#                 if email_of_registered_user:
#                     st.success('The new user has been successfully registered.')
#                     time.sleep(2)

#                     # Update the config with new credentials after registration
#                     with open('./config.yaml', 'w', encoding='utf-8') as file:
#                         yaml.dump(config, file, default_flow_style=False)

#             except stauth.RegisterError as e:
#                 st.error(f"Error registering user: {e}")

#     # Handle authentication status with custom messages based on login success or failure
#     if st.session_state.get("authentication_status"):
#         authenticator.logout('Logout', location='sidebar')
#         st.sidebar.success(f"Welcome back, {st.session_state['name']}!")
#     elif st.session_state.get("authentication_status") is False:
#         st.error('Username/password is incorrect')
#     elif st.session_state.get("authentication_status") is None:
#         st.warning('Please enter your username and password')

# # Function to render the page content based on navigation
# def display_page_content(page):
#     pages = {
#         "🏡 Home": "01_Home.py",
#         "📊 Data": "02_Data.py",
#         "📈 Dashboard": "03_Dashboard.py",
#         "🔮 Predictions": "04_Predict.py",
#         "🕰️ History": "05_History.py",
#     }

#     # # Dynamically load the selected page content
#     # if page in pages:
#     #     st.markdown(f"## {page}")
#     #     exec(open(pages[page]).read())

# # Main app logic to handle navigation after login
# def run_app():
#     # Set page configuration
#     st.set_page_config(page_title="Churn Prediction App", layout="wide", initial_sidebar_state="expanded")

#     # Display the login widget
#     display_login_and_register()

#     # If authenticated, display the main content and navigation
#     if st.session_state.get("authentication_status"):
#         # Sidebar for navigation
#         st.sidebar.title("Navigation")
#         pages = ["🏡 Home", "📊 Data", "📈 Dashboard", "🕰️ History", "🔮 Predictions"]
        
#         # Select page from the sidebar, default to "Home" after login
#         selected_page = st.sidebar.radio("Navigate to", pages, index=0)
        
#         # Automatically display the Home page after login and allow navigation via the sidebar
#         display_page_content(selected_page)

# if __name__ == "__main__":
#     run_app()




# import yaml
# import streamlit as st
# import streamlit_authenticator as stauth
# from yaml.loader import SafeLoader
# from streamlit_authenticator.utilities import LoginError
# import time

# # Function to load the YAML configuration file
# def load_app_config(config_path: str):
#     try:
#         with open(config_path, 'r', encoding='utf-8') as file:
#             config = yaml.load(file, Loader=SafeLoader)
#         return config
#     except FileNotFoundError:
#         st.error("Configuration file 'config.yaml' not found.")
#         st.stop()
#     except yaml.YAMLError as e:
#         st.error(f"Error loading YAML file: {e}")
#         st.stop()

# # Function to initialize the Streamlit Authenticator
# def setup_authenticator(config):
#     if 'authenticator' not in st.session_state:
#         st.session_state['authenticator'] = stauth.Authenticate(
#             config['credentials'],
#             config['cookie']['name'],
#             config['cookie']['key'],
#             config['cookie']['expiry_days'],
#             config['preauthorized']
#         )
#     return st.session_state['authenticator']

# # Function to display the login widget and handle authentication
# def display_login_and_register(page_title):
#     # Load the configuration and initialize the authenticator
#     config = load_app_config('./config.yaml')
#     authenticator = setup_authenticator(config)

#     # Display the login form if the user is not authenticated
#     if not st.session_state.get("authentication_status"):
#         st.title("🔐 Welcome to Churn Prediction App")
#         st.write("Please log in or register to continue.")
        
#         left_column, right_column = st.columns(2)
#         with left_column:
#             st.header("Login")
#             try:
#                 name, authentication_status, username = authenticator.login(location='main')
#             except LoginError as e:
#                 st.error(e)
        
#         with right_column:
#             st.header("Register")
#             try:
#                 email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
#                     location='main', pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'}
#                 )

#                 if email_of_registered_user:
#                     st.success('The new user has been successfully registered.')
#                     time.sleep(2)

#                     # Update the config with new credentials after registration
#                     with open('./config.yaml', 'w', encoding='utf-8') as file:
#                         yaml.dump(config, file, default_flow_style=False)

#             except stauth.RegisterError as e:
#                 st.error(f"Error registering user: {e}")

#     # Handle authentication status with custom messages based on the page title
#     if st.session_state.get("authentication_status"):
#         authenticator.logout('Logout', location='sidebar')
#         if page_title == "Home":
#             st.sidebar.success("How can we help you?👋🏾🙂")
#         elif page_title == "Data":
#             st.sidebar.success("Data ready for navigation 🧑🏾‍💻👍🏾")
#         elif page_title == "Dashboard":
#             st.sidebar.success("Explore the latest insights.🔎📶")
#         elif page_title == "History":
#             st.sidebar.success("View historical trends.⏳☎️")
#         elif page_title == "Predict":
#             st.sidebar.success("Make Predictions!🔭🤞🏾")
#         else:
#             st.sidebar.success("You're successfully logged in!")
#     elif st.session_state.get("authentication_status") is False:
#         st.error('Username/password is incorrect')
#     elif st.session_state.get("authentication_status") is None:
#         st.warning('Please enter your username and password')

# # Main app logic to handle navigation after login
# def run_app():
#     # Set page configuration
#     st.set_page_config(page_title="Churn Prediction App", layout="wide", initial_sidebar_state="expanded")

#     # Display the login widget and custom messages
#     display_login_and_register(page_title="Home")

#     # If authenticated, display the main content and navigation
#     if st.session_state.get("authentication_status"):
#         pages = {
#             "🏡 Home": "01_Home.py",
#             "📊 Data": "02_Data.py",
#             "📈 Dashboard": "03_Dashboard.py",
#             "🔮 Predictions": "04_Predict.py",
#             "🕰️ History": "05_History.py",
           
#         }

#         # Sidebar for navigation
#         selected_page = st.sidebar.radio("Navigate to", list(pages.keys()))

#         # Dynamically load the selected page content
#         if selected_page:
#             st.markdown(f"## {selected_page}")
#             exec(open(pages[selected_page]).read())

# if __name__ == "__main__":
#     run_app()
