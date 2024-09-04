import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

# Load the cleaned data
df = pd.read_csv('notebooks/cleaned_telecom_data.csv')

# Title of the app
st.title('Telecom Data Analysis')

# Sidebar for selecting features
st.sidebar.header('Feature Selection')
features = df.columns.tolist()
feature_x = st.sidebar.selectbox('Select X-axis feature', features)
feature_y = st.sidebar.selectbox('Select Y-axis feature', features)

# Scatter plot
st.subheader('Scatter Plot')
if feature_x and feature_y:
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[feature_x], y=df[feature_y], ax=ax)
    st.pyplot(fig)

# Correlation matrix
st.subheader('Correlation Matrix')
correlation_matrix = df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Histogram
st.subheader('Feature Distribution')
feature_hist = st.sidebar.selectbox('Select feature for histogram', features)
if feature_hist:
    fig, ax = plt.subplots()
    sns.histplot(df[feature_hist].dropna(), kde=True, ax=ax)
    st.pyplot(fig)

# Line plot (if date column exists)
if 'Date' in df.columns:
    st.subheader('Time Series Plot')
    feature_line = st.sidebar.selectbox('Select feature for time series', features)
    if feature_line:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='Date', y=feature_line, data=df, ax=ax)
        st.pyplot(fig)
else:
    st.write("No 'Date' column found for time series plot.")

# Close any open plots
plt.close('all')
