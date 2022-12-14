import streamlit as st
st.title('TITANIC SURVIVAL PREDICTION')
st.write('This app predicts the survival of passengers on the Titanic')
st.write('Data obtained from https://www.kaggle.com/c/titanic/data')
# Load the data'
import pandas as pd
df = pd.read_csv('titanic.csv')
# Show the data as a table
st.write(df)
# Show statistics
st.write(df.describe())
# Show the data as a chart
chart = st.bar_chart(df)
# Split the data into independent 'X' and dependent 'Y' variables
X = df.iloc[:, 1:8].values
Y = df.iloc[:, 0].values
# check the shape of data using streamlit
st.write(X.shape)
st.write(Y.shape)
# check how many null values are there in the data
st.write(df.isnull().sum())
