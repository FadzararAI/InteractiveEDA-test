import pandas as pd
import numpy as np

dataset = pd.read_csv("hotel.csv")

#Dropping columns which have highest mean of empty value
dataset.drop(dataset.columns[dataset.isnull().mean()>0.5], axis=1)

#Filling up null values of the dataset in 'agent' column with the mean
dataset['agent'].fillna(dataset['agent'].mean(), inplace=True)
#Filing up null values of the dataset in 'country' and 'children' columns
#with the data that appears most often
dataset['country'].fillna(dataset['country'].mode()[0], inplace=True)
dataset['children'].fillna(dataset['children'].mode()[0], inplace=True)

#Creating new columns based on certain conditions from 'lead_time' column
dataset["lead_time"] = np.where(dataset["lead_time"] < 122, 'Short', (np.where(dataset["lead_time"] < 245, 'Medium', 'Long')))

#Converting date from object into datetime data type
dataset["reservation_status_date"] = pd.to_datetime(dataset["reservation_status_date"])

#Saving the dataset into a new cleaned one
dataset.to_csv('hotel_cleaned.csv', date_format="%Y-%m-%d")