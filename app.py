#import necessary libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import random
#upload dataframe 
df = pd.read_csv('vehicles_us.csv')
#fill in the missing values
df['cylinders'] = df[['cylinders', 'type']].groupby('type').transform(lambda x:x.fillna(x.median()))
df['odometer'] = df.groupby('type')['odometer'].transform(lambda x: x.fillna(x.mean()))
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.mode().iloc[0]))
paint_color_list = df[~df['paint_color'].isna()]['paint_color'].to_list()
df['paint_color'] = df['paint_color'].fillna(random.choice(paint_color_list))
is_4wd_list = df[~df['is_4wd'].isna()]['is_4wd']
df['is_4wd'] = df['is_4wd'].fillna(random.choice(is_4wd_list))

#create a scatterplot that displays the how the the price of each car affects how long the car is listed for.  Add animation frame that displays the type and model of each car.
fig_scatter_1 = px.scatter(df, x= 'price', y='days_listed',color='condition', title="Relationship Between Car Price/ Car Quality and Days Listed", labels={'price': 'Car Price', 'days_listed': 'Number of Days Listed'},animation_frame='type', animation_group='model')

st.header('Project Title: Car Data Analysis')
#Display the dataframe on the application and create header.
st.header('US Vehicles Dataframe')
st.dataframe(df)


#Display the previously mentioned scatterplot on the application and add a header.
st.header('Car Price/Quality Analysis')
st.plotly_chart(fig_scatter_1)

#Filter all the unique values using the unique() function on the model column of the df dataframe.
model_unique = df['model'].unique()

#Create Selectbox with the model_unique variable previously created.
st.header("Car Model Count")
st.subheader("This histogram allows you to select and view the amount of cars listed by model and price.")
model_options = st.selectbox('Select Car Model', options=model_unique, index=0)

#Create a histogram that filters all the differnt types of car model in the model column of the df dataframe.
model_df = df[df['model']==model_options]
model_hist = px.histogram(model_df, x='price', nbins=20, height=600, width=900, title='Price of Cars Per Model')
st.write(model_hist)

#Add a checkbox using st.checkbox that displays the company phone number if checked.
st.header('Would you like to give our company a call?')
check = st.checkbox("Yes, I would like the company phone number!")
if check == True:
    st.write("Please call 1-800-4443 (This is not a real number)")