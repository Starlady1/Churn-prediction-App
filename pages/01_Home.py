
# import streamlit as st
# import yaml
# from yaml.loader import SafeLoader
# import time
# import streamlit_authenticator as stauth

#  # Set page configuration
# st.set_page_config(page_title="Home", page_icon="🏠",  layout="wide")

# with open('./config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# #create authenticator instance
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status,username = authenticator.login(location='sidebar')


# if st.session_state['authentication_status']:
#     authenticator.logout(location='sidebar')

#     # Add CSS for animations
#     st.write("""
#         <style>
#             @keyframes zoom-in {
#                 0% {
#                     transform: scale(0);
#                 }
#                 100% {
#                     transform: scale(1);
#                 }
#             }
#             @keyframes slide-in-right {
#                 0% {
#                     transform: translateX(100%);
#                 }
#                 100% {
#                     transform: translateX(0);
#                 }
#             }
#             @keyframes slide-in-left {
#                 0% {
#                     transform: translateX(-100%);
#                 }
#                 100% {
#                     transform: translateX(0);
#                 }
#             }
#             @keyframes slide-in-bottom {
#                 0% {
#                     transform: translateY(100%);
#                 }
#                 100% {
#                     transform: translateY(0);
#                 }
#             }
#             @keyframes slide-in-top {
#                 0% {
#                     transform: translateY(-100%);
#                 }
#                 100% {
#                     transform: translateY(0);
#                 }
#             }
#             .zoom-in-animation {
#                 animation: zoom-in 1.5s ease-in-out;
#             }
#             .slide-in-right-animation {
#                 animation: slide-in-right 1.5s ease-in-out;
#             }
#             .slide-in-left-animation {
#                 animation: slide-in-left 1.5s ease-in-out;
#             }
#             .slide-in-bottom-animation {
#                 animation: slide-in-bottom 1.5s ease-in-out;
#             }
#             .slide-in-top-animation {
#                 animation: slide-in-top 1.5s ease-in-out;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     # Header with zoom-in animation
#     st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Customer Churn Prediction App!</h1></div>', unsafe_allow_html=True)

#     # Content with different slide-in animations
#     st.write('<div class="slide-in-bottom-animation"><h3>Unleash the power of machine learning to predict customer churn!</h3></div>', unsafe_allow_html=True)

#     # Home Page Content
#     st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
#     st.markdown("""
#         <div class="slide-in-left-animation">
#             <p><span class="slide-in-bottom-animation">Welcome to the Customer Churn Prediction Application.</span> This tool is designed to help businesses in the telecommunications industry understand and predict customer churn. By leveraging advanced machine learning models, the application provides insights into customer behavior, identifies at-risk customers, and aids in the development of targeted retention strategies. This Home page serves as an entry point to the various features and functionalities offered by the application.</p>
#         </div>
#     """, unsafe_allow_html=True)

#     # Create columns for Key Features, How It Works
#     col1, col2= st.columns(2)

#     # Key Features with slide-in-right animation
#     with col1:
#      st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
#      st.markdown("## Key Features")
#      st.markdown("""
#         - **Data Exploration:** The Data page allows users to explore the customer churn dataset. Users can view detailed descriptions of each column, filter data based on specific criteria, and get a comprehensive understanding of the dataset's structure.
#         - **Account Page:** Manage your personal account settings, including updating details, resetting passwords, and handling user registrations.
#         - **Interactive Dashboard:** The Dashboard page offers a variety of visualizations and key performance indicators (KPIs) to help users analyze customer churn data. The interactive charts and graphs enable users to uncover trends and patterns that influence customer churn.
#         - **Customer Churn Prediction:** On the Predict page, users can input customer details to predict the likelihood of churn. The page supports both individual predictions and bulk predictions via CSV or Excel file uploads. Users can select from multiple pre-trained machine learning models to generate predictions.
#         - **Historical Predictions:** The History page provides a log of all past predictions. This feature allows users to review previous predictions, analyze trends over time, and assess the performance of different predictive models.     
#         """)
#     st.markdown('</div>', unsafe_allow_html=True)    

#     # How It Works with slide-in-bottom animation
#     with col2:
#      st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
#      st.markdown("## How It Works")
#      st.markdown("""
        
#         1. **Data Loading and Exploration:**
#            - `Data Page:` Loading the Dataset: Loads the customer churn dataset (CSV) into a Pandas DataFrame.
#            - `Exploration Tools:` Users can explore the dataset, view column descriptions, and filter data by type (numeric or categorical).
        
#         2. **Interactive Dashboard:**
#            - `Visual Insights:` Provides visualizations to analyze customer churn data, showing KPIs and trends.
#            - `Filters and Customization:` Users can apply filters (e.g., Gender, Payment Method) to customize visualizations for deeper analysis.
        
#         3. **Customer Churn Prediction:**
#            - `User Input:` Users input customer details like demographics and billing info.
#            - `Model Selection:` Loads pre-trained models (e.g., Logistic Regression, AdaBoost) for prediction.
#            - `Prediction:` Predicts churn likelihood and probability based on user input.
#            - `Bulk Prediction:` Allows batch processing by uploading CSV/Excel files with multiple customer records.
        
#         4. **Historical Predictions:**
#            - `Record Keeping:` Logs all past predictions, including customer attributes, outcomes, probabilities, models used, and prediction times.
#            - `Analysis and Insights:` Users can review historical data to identify patterns and validate model consistency
        
#         5. **Authentication and User Management:**
#            - `Secure Access:` Ensures only authenticated users can access sensitive data and tools.
#            - `Session Management:` Manages user sessions for a seamless and secure experience.
#         """)
#     st.markdown('</div>', unsafe_allow_html=True)
  

#     st.markdown('<div class="slide-in-top-animation">', unsafe_allow_html=True)
#     st.markdown("""
#     The Customer Churn Prediction Application is a comprehensive tool designed to help businesses reduce churn rates and improve customer retention. By integrating data exploration, interactive dashboards, predictive modeling, and historical analysis, the application provides a robust framework for understanding and addressing customer churn. Explore the features and functionalities of this application to gain actionable insights and make data-driven decisions for your business        """)
#     st.markdown('</div>', unsafe_allow_html=True)


#     st.header("About the Developer")
#     st.write("**Name:** Fanen Stella")
#     st.write("**Background:** Expert in data science, machine learning, and software development.")
#     st.write("**Contact:** www.linkedin.com/in/tamminga-givondo/")
    
#     # Footer
#     st.markdown("""
#         ---
#         © 2024 Customer Churn Prediction Project. All rights reserved.
#     """)

# # Handle user registration if the user is not authenticated
# elif authentication_status is None:
#     st.info('Please Login or Register to Proceed')
    
#     # Handle user registration
#     try:
#         email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(
#             "sidebar", pre_authorization=False, fields={'Form name': 'Sign Up Here', 'Register': 'Sign Up'}
#         )

#         if email_of_registered_user:
#             success_placeholder = st.empty()
#             success_placeholder.success('The new user has been successfully registered.')
#             time.sleep(3)
#             success_placeholder.empty()

#         # Update the config with new credentials if registration is successful
#         with open('./config.yaml', 'w', encoding='utf-8') as file:
#             yaml.dump(config, file, default_flow_style=False)

#     except stauth.RegisterError as e:
#         st.error(f"Error registering user: {e}")

# # If login is unsuccessful (wrong credentials)
# else:
#     st.error('Wrong username or password')


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
    st.write("**Name:** Fanen Stella")
    st.write("**Background:** Expert in data science, machine learning, and software development.")
    st.write("**Contact:** www.linkedin.com/in/tamminga-givondo/")
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




