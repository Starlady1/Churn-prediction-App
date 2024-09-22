import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import warnings
warnings.filterwarnings('ignore')


def dashboard_page():
    # Check authentication
    if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
        # 1. Add CSS for title styling and zoom-in animation
        st.write("""
        <style>
            @keyframes zoom-in {
                0% {
                    transform: scale(0);
                }
                100% {
                    transform: scale(1);
                }
            }
            .zoom-in-animation {
                animation: zoom-in 3s ease-in-out;
            }
            .dashboard-title {
                font-size: 48px;
                font-weight: bold;
                color: #4b8bbe; /* Light blue */
                text-shadow: 2px 2px #d3e3f1; /* Subtle shadow for a 3D effect */
                margin-bottom: 10px;
                position: relative;
                display: inline-block;
            }
            .dashboard-title::before {
                content: "📊"; /* Adding an icon before the title */
                font-size: 48px;
                margin-right: 10px;
            }
            .dashboard-title::after {
                content: "";
                position: absolute;
                width: 100%;
                left: 0;
                bottom: -5px; /* Adjust this value as needed */
                border-bottom: 4px solid #4b8bbe;
            }
        </style>
        """, unsafe_allow_html=True)

        # Dashboard title
        st.title("Customer Churn Dashboard")

        # Overview Section
        st.header("Overview")
        st.markdown("""
        This dashboard provides insights into customer churn data, helping you understand the factors influencing churn and make data-driven decisions to improve customer retention.
        """)

        # 2. Load your dataset
        data = pd.read_csv('Data/churn_data.csv')

        # Drop unnecessary column
        data.drop('customerID', axis=1, inplace=True)

        # 3. Filters
        st.sidebar.subheader("Dashboard Filters")

        # Create for Gender
        gender = st.sidebar.multiselect("Pick your Gender", data["gender"].unique())
        filtered_data = data.copy() if not gender else data[data["gender"].isin(gender)]

        # Create for payment type
        paymentmethod = st.sidebar.multiselect("Pick your Payment Method", data["PaymentMethod"].unique())
        if paymentmethod:
            filtered_data = filtered_data[filtered_data["PaymentMethod"].isin(paymentmethod)]

        # Create for Contract type
        contract = st.sidebar.multiselect("Pick your Contract", data["Contract"].unique())
        if contract:
            filtered_data = filtered_data[filtered_data["Contract"].isin(contract)]

        # 4. Define EDA Function
        def eda_dash():
            # Add CSS for EDA title animation
            st.write("""
                <style>
                    @keyframes zoom-in {
                        0% {
                            transform: scale(0);
                        }
                        100% {
                            transform: scale(1);
                        }
                    }
                    .zoom-in-animation {
                        animation: zoom-in 3s ease-in-out;
                    }
                </style>
            """, unsafe_allow_html=True)

            # Add an animated text
            st.write('<div class="zoom-in-animation"><h3>Delve into Exploratory Data Analysis Insights</h3></div>', unsafe_allow_html=True)

            # 4.1 Scatter Plot with conditional coloring
            scatter_plot = px.scatter(
                filtered_data,
                x='tenure',
                y='MonthlyCharges',
                color='Churn',
                color_discrete_map={'yes': 'red', 'no': 'skyblue'},
                title='Scatter Plot for Tenure vs Monthly Charges'
            )
            scatter_plot.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=2, color='DarkSlateGrey')))
            st.plotly_chart(scatter_plot)

            # 4.2 Histograms
            col1, col2 = st.columns(2)
            with col1:
                fig = px.histogram(filtered_data, x="tenure", color="Churn", marginal="box", nbins=50, title="Histogram for Tenure")
                st.plotly_chart(fig)
            with col2:
                fig = px.histogram(filtered_data, x="MonthlyCharges", color="Churn", marginal="box", nbins=50, title="Histogram for Monthly Charges")
                st.plotly_chart(fig)

            # 4.3 Correlation Matrix and Heatmap for Numeric Variables
            numeric_columns = filtered_data.select_dtypes(include=['number']).columns
            numeric_df = filtered_data[numeric_columns]
            numeric_correlation_matrix = numeric_df.corr()

            fig = px.imshow(
                numeric_correlation_matrix.values,
                x=numeric_correlation_matrix.columns,
                y=numeric_correlation_matrix.columns,
                labels=dict(color="Correlation"),
                color_continuous_scale='RdBu',
                zmin=-1, zmax=1
            )

            fig.update_layout(title='Correlation Matrix Heatmap', xaxis_title="Numeric Variables", yaxis_title="Numeric Variables", width=800, height=600)

            annotations = []
            for i, row in enumerate(numeric_correlation_matrix.values):
                for j, value in enumerate(row):
                    annotations.append(dict(x=numeric_correlation_matrix.columns[j], y=numeric_correlation_matrix.index[i],
                                            text=f"{value:.2f}", showarrow=False, font=dict(color='black')))
            fig.update_layout(annotations=annotations)
            st.plotly_chart(fig)

            # 4.4 Trend of average monthly charges by tenure
            avg_monthly_charges = filtered_data.groupby('tenure')['MonthlyCharges'].mean().reset_index()
            fig = px.line(avg_monthly_charges, x='tenure', y='MonthlyCharges', title='Average Monthly Charges Trend by Tenure')
            fig.update_layout(xaxis_title='Tenure', yaxis_title='Average Monthly Charges', width=800, height=500)
            st.plotly_chart(fig)

            # Calculate churn rate by tenure
            churn_counts = filtered_data.groupby('tenure')['Churn'].value_counts().unstack(fill_value=0)
            churn_counts['Churn Rate'] = churn_counts['Yes'] / churn_counts.sum(axis=1) * 100
            churn_counts = churn_counts.reset_index()

            fig = px.line(churn_counts, x='tenure', y='Churn Rate', title='Churn Rate by Tenure')
            fig.update_layout(xaxis_title='Tenure', yaxis_title='Churn Rate (%)', width=800, height=500)
            st.plotly_chart(fig)

        #Define the KPI function
        def kpi_dash():
            # Apply zoom-in animation styling
            st.write("""
                <style>
                    @keyframes zoom-in {
                        0% { transform: scale(0); }
                        100% { transform: scale(1); }
                    }
                    .zoom-in-animation {
                        animation: zoom-in 1.5s ease-in-out;
                        text-align: center;
                        margin-bottom: 20px;
                    }
                </style>
            """, unsafe_allow_html=True)
    
            st.write('<div class="zoom-in-animation"><h2 style="color:#1f77b4;">📊 Key Performance Indicators Insights</h2></div>', unsafe_allow_html=True)

            # Sample filtered data for illustration
            total_customers = len(filtered_data)
            churned_customers = (filtered_data['Churn'] == 'Yes').sum()
            churn_rate = (churned_customers / total_customers) * 100
            avg_monthly_charge = filtered_data['MonthlyCharges'].mean()
            avg_total_charge = filtered_data['TotalCharges'].mean()
            avg_tenure = filtered_data['tenure'].mean()

            # Custom card styling for KPIs
            st.write("""
                <style>
                    .kpi-card {
                        background-color: #f0f0f5; 
                        padding: 15px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                        text-align: center;
                        margin: 10px;
                        width: 220px;
                        transition: transform 0.2s;
                    }
                    .kpi-card:hover {
                        transform: translateY(-5px);
                    }
                    .kpi-title {
                        font-size: 18px;
                        font-weight: 600;
                        color: #333333;
                    }
                    .kpi-value {
                        font-size: 24px;
                        font-weight: bold;
                        color: #007bff;
                        margin-top: 5px;
                    }
                </style>
            """, unsafe_allow_html=True)

            # Display KPIs in two rows using columns for better layout
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Total Customers 👫</div><div class='kpi-value'>{total_customers}</div></div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Churned Customers 🚶‍♂️🚶‍♀️</div><div class='kpi-value'>{churned_customers}</div></div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Churn Rate 📈</div><div class='kpi-value'>{churn_rate:.2f}%</div></div>", unsafe_allow_html=True)

            col4, col5, col6 = st.columns([1, 1, 1])
            with col4:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg. Monthly Charge 💰</div><div class='kpi-value'>${avg_monthly_charge:.2f}</div></div>", unsafe_allow_html=True)
            with col5:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg. Total Charge 💳</div><div class='kpi-value'>${avg_total_charge:.2f}</div></div>", unsafe_allow_html=True)
            with col6:
                st.markdown(f"<div class='kpi-card'><div class='kpi-title'>Avg. Tenure 📅</div><div class='kpi-value'>{avg_tenure:.2f} months</div></div>", unsafe_allow_html=True)

            # Display a gauge for the churn rate
            st.subheader("Churn Rate Gauge")
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=churn_rate,
                title={'text': "Churn Rate (%)"},
                gauge={'axis': {'range': [0, 100]},
                    'bar': {'color': "#1f77b4"},
                    'steps': [
                        {'range': [0, 25], 'color': "#d4edda"},
                        {'range': [25, 50], 'color': "#ffeeba"},
                        {'range': [50, 75], 'color': "#f8d7da"},
                        {'range': [75, 100], 'color': "#f5c6cb"}],
                    'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': churn_rate}}))

            fig.update_layout(height=400, margin={'t': 50, 'b': 0, 'l': 0, 'r': 0})
            st.plotly_chart(fig)

        # Define Menu
        menu = st.sidebar.radio("Select a Page:", ("Exploratory Data Analysis", "Key Performance Indicators"))

        if menu == "Exploratory Data Analysis":
            eda_dash()  # Assuming this function is already defined
        elif menu == "Key Performance Indicators":
            kpi_dash()

    else:
        st.warning("Please log in to access this page.")

# Call the dashboard_page function
if __name__ == "__main__":
    dashboard_page()

