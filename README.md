Project Description:  This application is named 'Car Data Analysis'.  This application contains: a display of the
full vehicles_us dataframe, a scatterplot titled: 'Car Price/Quality Analysis' which displays the relationship between the car price/quality and the number of days listed in order to show whether car price or car quality affects sales, a histogram titled: 'Car Model Count' which displays the amount of cars listed in the company according to car model and price, and a checkbox which displays the company phone number(fake number) if the box is checked.

Libraries imported:  Pandas in order to import the dataframe.  Streamlit in order to run the application.  Plotly Express in order to display the chart.

List of functions used:
Python:
* fillna() - in order to fill in missing values in the dataframe
* unique() - in order to display all unique values
Pandas:
* pd.read_csv() - in order to import the dataframe
Plotly Express:
* px.scatter() - in order to create the scatterplot
* px.histogram() - in order to create the histogram
Streamlit:
* st.header() - in order to display a header with text
* st.write() -
* st.subheader() - in order to display a subheader with text
* st.dataframe() - in order to display dataframe on the app
* st.selectbox() - in order to display selectbox on the app
* st.checkbox() - in order to display checkboxes on the app
* st.plotly_chart() - in order to display charts from plotly express on the app

Special Arguements:
* animation_frame= and animation_group= to px.scatter() in order to make animated scatterplot

Instructions on how to run the app
Type in the following command in the terminal:

streamlit run app.py

Render URL:
https://sprint-4-project-7bdr.onrender.com/