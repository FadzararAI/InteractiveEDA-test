import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Dataset loading
dataset_cleaned = pd.read_csv("Data_cleaning\\hotel_cleaned.csv")
dataset_cleaned.drop('Unnamed: 0', axis = 1, inplace = True)

st.write("""
# Explanatory Data Analysis of Hotel Reservation Dataset
Below is the dataset as well as the graphs to showcase and see the dataset.
	""")

#Dataset filtering widget (sidebar)
with st.sidebar:
	st.subheader("Dataset Filters")
	reservation = st.radio("Reservation Date", options = list(dataset_cleaned['arrival_date_year'].drop_duplicates()))
	lead = st.radio("Lead Time", options = list(dataset_cleaned['lead_time'].drop_duplicates()))
#Filtered Dataset
dataset_cleaned.loc[(dataset_cleaned['lead_time'] == lead) & (dataset_cleaned['reservation_status_date'] >= str(reservation))]

#Dataset Visualization
st.write("""
## Dataset Visualization
Below are the visualizations by Bar for the dataset
	""")
#Defining necessary data to visualize
months = list(dataset_cleaned['arrival_date_month'].value_counts().index)
amounts = list(dataset_cleaned['arrival_date_month'].value_counts().values)

# Vertical bar visualization
fig = plt.figure(figsize=(13,6))
plt.bar(months,amounts)
plt.title("Most Visitors By Month")
plt.ylabel("Visitors")
plt.xlabel("Months")
st.pyplot(fig)
st.write("Horizontal bar visualization")
# Horizontal bar visualization
fig = plt.figure(figsize=(12,8))
plt.barh(months,amounts)
plt.title("Most Visitors By Month")
plt.ylabel("Months")
plt.xlabel("Visitors")
plt.gca().invert_yaxis()
st.pyplot(fig)