import streamlit as st
import pandas as pd

# Load Data
@st.cache_data  # the new updated streamlit data caching decorator.
def load_data():
    # df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/MohamedSalah-GitHub/Covid-19_Streamlit_App/refs/heads/main/WHO-COVID-19-global-data.csv')
    df['Date_reported'] = pd.to_datetime(df['Date_reported'])
    return df

df = load_data()

# About Data
st.title('About Data')
st.markdown('''
This app is created to analyze the Covid-19 data.
''')

# Display Data
st.header('Data')
if st.checkbox('Show Data'):
    st.write(df)
