import streamlit as st
import pandas as pd
from streamlit_modal import Modal
import os

# Set page configuration
st.set_page_config(page_title="Data", page_icon='🗄️', layout="wide")

if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
    st.title("Customer Churn Dataset")

    # Dictionary with column descriptions
    columns_description = {
        "Gender": "Whether the customer is a male or a female",
        "SeniorCitizen": "Whether a customer is a senior citizen or not",
        "Partner": "Whether the customer has a partner or not (Yes, No)",
        "Dependents": "Whether the customer has dependents or not (Yes, No)",
        "Tenure": "Number of months the customer has stayed with the company",
        "Phone Service": "Whether the customer has a phone service or not (Yes, No)",
        "MultipleLines": "Whether the customer has multiple lines or not",
        "InternetService": "Customer's internet service provider (DSL, Fiber Optic, No)",
        "OnlineSecurity": "Whether the customer has online security or not (Yes, No, No Internet)",
        "OnlineBackup": "Whether the customer has online backup or not (Yes, No, No Internet)",
        "DeviceProtection": "Whether the customer has device protection or not (Yes, No, No Internet)",
        "TechSupport": "Whether the customer has tech support or not (Yes, No, No Internet)",
        "StreamingTV": "Whether the customer has streaming TV or not (Yes, No, No Internet)",
        "StreamingMovies": "Whether the customer has streaming movies or not (Yes, No, No Internet)",
        "Contract": "The contract term of the customer (Month-to-Month, One year, Two year)",
        "PaperlessBilling": "Whether the customer has paperless billing or not (Yes, No)",
        "Payment Method": "The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))",
        "MonthlyCharges": "The amount charged to the customer monthly",
        "TotalCharges": "The total amount charged to the customer",
        "Churn": "Whether the customer churned or not (Yes or No)"
    }

    # Two columns layout
    col1, col2 = st.columns(2)

    with col1:
        # Dropdown menu to select a column
        selected_column = st.selectbox("Select a column to see its description:", list(columns_description.keys()))

        # Display selected column description
        st.markdown(f"**{selected_column}**: {columns_description[selected_column]}")

    with col2:
        def filter_columns(data):
            # Dropdown menu to filter columns by type
            data_type = st.selectbox('Select Data Type:', ['All', 'Numeric Columns', 'Categorical Columns'])

            # Filter the data based on the selected data type
            if data_type == 'Numeric Columns':
                data = data.select_dtypes(include=['number'])
            elif data_type == 'Categorical Columns':
                data = data.select_dtypes(include=['object', 'category'])

            # Display the filtered data
            st.write(data)

    # Define the path to the dataset
    dataset_path = 'Data/churn_data.csv'

    # Check if the file exists
    if not os.path.isfile(dataset_path):
        st.error(f"The file '{dataset_path}' does not exist. Please check the path.")
    else:
        try:
            # Load the dataset
            data = pd.read_csv(dataset_path)
            data = data.drop('Unnamed: 0', axis=1)  # Remove unwanted column if needed
            
            # Call the function to filter and display columns
            filter_columns(data)
        except Exception as e:
            st.error(f"Error loading the file '{dataset_path}': {e}")

else:
    st.warning('Please login to access this page')








# import streamlit as st
# import pandas as pd
# from streamlit_modal import Modal
# import os

# # Set page configuration
# st.set_page_config(page_title="Data", page_icon = '🗄️', layout="wide")

# if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
#     st.title("Customer Churn Dataset")

#     columns_description = {
#         "Gender": "Whether the customer is a male or a female",
#         "SeniorCitizen": "Whether a customer is a senior citizen or not",
#         "Partner": "Whether the customer has a partner or not (Yes, No)",
#         "Dependents": "Whether the customer has dependents or not (Yes, No)",
#         "Tenure": "Number of months the customer has stayed with the company",
#         "Phone Service": "Whether the customer has a phone service or not (Yes, No)",
#         "MultipleLines": "Whether the customer has multiple lines or not",
#         "InternetService": "Customer's internet service provider (DSL, Fiber Optic, No)",
#         "OnlineSecurity": "Whether the customer has online security or not (Yes, No, No Internet)",
#         "OnlineBackup": "Whether the customer has online backup or not (Yes, No, No Internet)",
#         "DeviceProtection": "Whether the customer has device protection or not (Yes, No, No Internet)",
#         "TechSupport": "Whether the customer has tech support or not (Yes, No, No Internet)",
#         "StreamingTV": "Whether the customer has streaming TV or not (Yes, No, No Internet)",
#         "StreamingMovies": "Whether the customer has streaming movies or not (Yes, No, No Internet)",
#         "Contract": "The contract term of the customer (Month-to-Month, One year, Two year)",
#         "PaperlessBilling": "Whether the customer has paperless billing or not (Yes, No)",
#         "Payment Method": "The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))",
#         "MonthlyCharges": "The amount charged to the customer monthly",
#         "TotalCharges": "The total amount charged to the customer",
#         "Churn": "Whether the customer churned or not (Yes or No)"
#     }

#     col1, col2 = st.columns(2)
#     with col1:
#     # Create a dropdown menu for column selection
#         selected_column = st.selectbox("Select a column to see its description:", list(columns_description.keys()))

#     # Display the description of the selected column
#     st.markdown(f"**{selected_column}**: {columns_description[selected_column]}")
#     with col2:
#         def filter_columns(data):
#         # Allow the user to select the data type to display

#             data_type = st.selectbox('Select Data type', [
#                                 'All', 'Numeric Columns', 'Categorical Columns'])

#             if data_type == 'Numeric Columns':
#                 data = data.select_dtypes(include=['number'])
#             elif data_type == 'Categorical Columns':
#                 data = data.select_dtypes(include=['object', 'category'])

#         # Display the filtered data in Streamlit
#             st.write(data)


#     # Define the path to the dataset
#     dataset_path = 'Data/churn_data.csv'

#     # Check if the file exists
#     if not os.path.isfile(dataset_path):
#         st.error(
#             f"The file '{dataset_path}' does not exist. Please check the path.")
#     else:
#         try:
#             # Load the dataset
#             data = pd.read_csv(dataset_path)
#             data = data.drop('Unnamed: 0', axis =1)
#             # st.write('Loaded Data:', data)
#             # Call the function to filter and display columns
#             filter_columns(data)
#         except Exception as e:
#             st.error(f"Error loading the file '{dataset_path}': {e}")

# else:
#     st.warning('Please login to access this page')