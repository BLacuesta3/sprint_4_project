import pandas as pd
import streamlit as st
df = pd.read_csv('vehicles_us.csv')
st.write(df.head())