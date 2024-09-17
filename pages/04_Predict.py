import streamlit as st
import pandas as pd
import joblib
import os
import datetime
import pickle as pl
from sklearn.preprocessing import LabelEncoder

# Set page configuration
st.set_page_config(page_title="Predict", page_icon="🔮", layout="wide")

if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
    st.title("Predict Customer Churn!")

    # Load models and encoder
    @st.cache_resource(show_spinner='Loading Gradient Boosting Model...')
    def load_gradient_boosting_pipeline():
        return joblib.load('./Models/best_gbc_tuned.joblib')

    @st.cache_resource(show_spinner='Loading Random Forest Model...')
    def load_random_forest_pipeline():
        return joblib.load('./Models/best_rf_model.joblib')
         
    @st.cache_resource(show_spinner='Loading Encoder...')
    def load_and_fit_encoder(encoder_path='./Models/label_encoder.joblib', labels=['No', 'Yes']):
        try:
            # Load the encoder from the file
            encoder = joblib.load(encoder_path)
            # Check if the encoder is already fitted by checking for the 'classes_' attribute
            if not hasattr(encoder, 'classes_'):
                # If not fitted, fit it with the provided labels
                encoder.fit(labels)
                # Optionally, save the fitted encoder back to the file
                joblib.dump(encoder, encoder_path)
            return encoder
        except FileNotFoundError:
         # If the encoder file doesn't exist, create a new LabelEncoder and fit it
            encoder = LabelEncoder()
            encoder.fit(labels)
            # Save the newly created and fitted encoder
            joblib.dump(encoder, encoder_path)
            return encoder

    # def select_model(key):
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         st.selectbox('Select a model', ['Gradient Boosting', 'Random Forest'], key=key)

    #     if st.session_state[key] == 'Gradient Boosting':
    #         pipeline = load_gradient_boosting_pipeline()
    #         threshold = None  # No threshold for Gradient Boosting

    #     else:
    #         pipeline, threshold = load_random_forest_pipeline()  # Get both model and threshold
    def select_model(key):
        col1, col2 = st.columns(2)
        with col1:
            selected_model = st.selectbox('Select a model', ['Gradient Boosting', 'Random Forest'], key=key)

        if selected_model == 'Gradient Boosting':
            pipeline = load_gradient_boosting_pipeline()
        else:
            pipeline = load_random_forest_pipeline()  # Get both model 
        # Debug: Print the type of pipeline
        st.write(f"Selected model: {selected_model}, Type of pipeline: {type(pipeline)}")

    # Load and fit the encoder
        encoder = load_and_fit_encoder(encoder_path='./Models/label_encoder.joblib', labels=['No', 'Yes'])
        return pipeline, encoder
        # # Load and fit the encoder
        # encoder = load_and_fit_encoder(encoder_path='./Models/label_encoder.joblib', labels=['No', 'Yes'])
        # return pipeline, threshold, encoder

    def make_prediction(pipeline, encoder):
        if not pipeline:
            st.error("No model pipeline loaded!")
            return

        # Collect user input from session state
        user_input = {
            'gender': st.session_state['gender'],
            'SeniorCitizen': st.session_state['senior_citizen'],
            'Partner': st.session_state['partner'],
            'Dependents': st.session_state['dependents'],
            'tenure': st.session_state['tenure'],
            'PhoneService': st.session_state['phone_service'],
            'MultipleLines': st.session_state['multiple_lines'],
            'InternetService': st.session_state['internet_service'],
            'OnlineSecurity': st.session_state['online_security'],
            'OnlineBackup': st.session_state['online_backup'],
            'DeviceProtection': st.session_state['device_protection'],
            'TechSupport': st.session_state['tech_support'],
            'StreamingTV': st.session_state['streaming_tv'],
            'StreamingMovies': st.session_state['streaming_movies'],
            'Contract': st.session_state['contract'],
            'PaperlessBilling': st.session_state['paperless_billing'],
            'PaymentMethod': st.session_state['payment_method'],
            'MonthlyCharges': st.session_state['monthly_charges'],
            'TotalCharges': st.session_state['total_charges'],
        }

        # Make a DataFrame
        df = pd.DataFrame(user_input, index=[0])

        # Debug: Print pipeline to verify it's the correct model
        st.write(f"Pipeline: {pipeline}")

        # Define Probability and Prediction
        pred = pipeline.predict(df)
        pred_int = int(pred[0])

        # Check if the encoder is fitted
        if not hasattr(encoder, 'classes_'):
            st.error("The LabelEncoder instance is not fitted. Please fit the encoder with the appropriate classes before using.")
            return
        
        # Define Probability and Prediction
        pred_proba = pipeline.predict_proba(df)[0]

       
        prediction = encoder.inverse_transform([pred_int])[0]

        # Calculate the probability of churn
        probability = pipeline.predict_proba(df)[0][pred_int] * 100
        st.session_state['prediction'] = prediction
        st.session_state['probability'] = probability

        # Save prediction history
        df['prediction'] = prediction
        df['probability'] = probability
        df['time_of_prediction'] = datetime.date.today()
        df['model_used'] = st.session_state['selected_model']

        # Save the results to a CSV file
        df.to_csv("Data/history.csv", mode='a', header=not os.path.exists("Data/history.csv"))

        return prediction, probability

    def display_form():
        pipeline, encoder = select_model(key='selected_model')

        with st.form('input_features'):
            col1, col2 = st.columns(2)

            with col1:
                st.write('### Customer Demographics')
                st.selectbox('Gender', options=['Male', 'Female'], key='gender')
                st.selectbox('Senior Citizen', options=['Yes', 'No'], key='senior_citizen')
                st.selectbox('Partner', options=['Yes', 'No'], key='partner')
                st.selectbox('Dependents', options=['Yes', 'No'], key='dependents')
                st.number_input('Tenure (months)', min_value=0, max_value=100, step=1, key='tenure')

                st.write('### Billing and Payment')
                st.selectbox('Paperless Billing', options=['Yes', 'No'], key='paperless_billing')
                st.selectbox('Payment Method', options=[
                    'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
                ], key='payment_method')
                st.number_input('Monthly Charges ($)', min_value=0.0, format="%.2f", step=1.00, key='monthly_charges')
                st.number_input('Total Charges ($)', min_value=0.0, format="%.2f", step=1.00, key='total_charges')

            with col2:
                st.write('### Services Subscribed')
                st.selectbox('Phone Service', options=['Yes', 'No'], key='phone_service')
                st.selectbox('Multiple Lines', options=['Yes', 'No'], key='multiple_lines')
                st.selectbox('Internet Service', options=['DSL', 'Fiber optic', 'No'], key='internet_service')
                st.selectbox('Online Security', options=['Yes', 'No'], key='online_security')
                st.selectbox('Online Backup', options=['Yes', 'No'], key='online_backup')
                st.selectbox('Device Protection', options=['Yes', 'No'], key='device_protection')
                st.selectbox('Tech Support', options=['Yes', 'No'], key='tech_support')
                st.selectbox('Streaming TV', options=['Yes', 'No'], key='streaming_tv')
                st.selectbox('Streaming Movies', options=['Yes', 'No'], key='streaming_movies')
                st.selectbox('Contract', options=['Month-to-month', 'One year', 'Two year'], key='contract')

            st.form_submit_button('Submit', on_click=make_prediction, kwargs={'pipeline': pipeline, 'encoder': encoder})

    if 'prediction' not in st.session_state:
        st.session_state['prediction'] = None
    if 'probability' not in st.session_state:
        st.session_state['probability'] = None

    tab1, tab2 = st.tabs(['Predict', 'Bulk Predict'])

    with tab1:
        display_form()

        final_prediction = st.session_state['prediction']
        final_probability = st.session_state['probability']

        if final_prediction is None:
            st.write('Predictions will show here!')
        else:
            if final_prediction.lower() == 'yes':
                st.markdown(f'### Customer will leave 😞.')
                st.markdown(f'## Probability: {final_probability:.2f}%')
            else:
                st.markdown(f'### Customer will stay 😊.')
                st.markdown(f'## Probability: {final_probability:.2f}%')

    with tab2:
        pipeline_bulk, encoder_bulk = select_model(key='selected_model_bulk')

        # File uploader for bulk predictions
        uploaded_file = st.file_uploader("Choose a CSV or Excel File", type=['csv', 'xls', 'xlsx'])
        if uploaded_file is not None:
            file_extension = uploaded_file.name.split('.')[-1]

            if file_extension == 'csv':
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.write(df)

            # Preprocess the data
            df.drop('CustomerID', axis=1, inplace=True)
            df.columns = df.columns.str.lower()
            df['Totalcharges'] = pd.to_numeric(df['Totalcharges'], errors='coerce')

            # Predict
            pred = pipeline_bulk.predict(df)
            prediction = encoder_bulk.inverse_transform(pred)
            probability = pipeline_bulk.predict_proba(df) * 100

            df['Churn'] = prediction
            df['probability'] = probability.max(axis=1)

            st.subheader("The Dataframe with predicted churn")
            st.write(df)

else:
    st.warning('Please login to access this page')





