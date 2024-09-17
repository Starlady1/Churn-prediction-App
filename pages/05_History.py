import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='Predict Customer Churn!',
    page_icon='🔮',
    layout='wide'
)
if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
    def display_history_prediction():

        csv_path = "Data/history.csv"
        csv_exists = os.path.exists(csv_path)

        if csv_exists:
            history = pd.read_csv(csv_path)
            # Check if 'Unnamed: 0' exists and drop it
            if 'Unnamed: 0' in history.columns:
                history = history.drop('Unnamed: 0', axis =1)
            st.dataframe(history)


    if __name__ == '__main__':
        st.title('History Page')
        display_history_prediction()

else:
    st.warning('Please login to access this page')