#import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px
#upload dataframe and fill in missing values with 'unknown'
df = pd.read_csv('vehicles_us.csv')
df.fillna('unknown', inplace=True)

#create a scatterplot that displays the how the the price of each car affects how long the car is listed for.
fig_scatter_1 = px.scatter(df, x= 'price', y='days_listed',color='condition', title="Relationship Between Car Price/ Car Quality and Days Listed", labels={'price': 'Car Price', 'days_listed': 'Number of Days Listed'})
#create a histogram that counts the amount of listings for each car model in the lot.
fig_hist_1 = px.histogram(df,x='model', nbins=20, height=600, width=900, title='Number of Cars in Lot per Model')

#Display the dataframe on the application and create header.
st.header('US Vehicles Dataframe')
st.dataframe(df)

#check = st.checkbox() *Code for the checkbox.
#Display the previously mentioned scatterplot on the application and add a header.
st.header('Car Price/Quality Analysis')
st.plotly_chart(fig_scatter_1)
#Display the previously mentioned histogram on the application and add a header.
st.header('Car Model Count Histogram')
st.plotly_chart(fig_hist_1)

st.header('Would you like to give our company a call?')
check = st.checkbox("Yes, I would like the company phone number!")
if check == True:
    st.write("Please call 1-800-4443 (This is not a real number)")