# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:59:29 2021

@author: asjya
"""

import pandas as pd 

import os
path = ".\data"
filename = 'Bicycle_Thefts.csv'
fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)
print(bike_df)
pd.set_option('display.max_columns',15)
print(bike_df.head())
print(bike_df.columns.values)
print(bike_df.shape)
print(bike_df.describe())
print(bike_df.dtypes) 
print(bike_df.head(5))

print("# of Null Values: \n")
print(bike_df.isnull().sum())


print('\n Mean of Numerical Columns: \n')
print(bike_df.mean())
'''
There are 35 columns and 25569 rows in the bike dataframe. 
2 Columns should be datetime but are coming out as string. We can clean this up
Bike_Make, Bike_Model, Bike_Colour, and Cost_of_Bike have numerous null values that we need to handle.
''' 

print('\n Mode of Categorical Columns: \n')
print(bike_df[bike_df.select_dtypes(include=['object']).columns.tolist()].mode())

'''
Convert the Obejct Data type of the Occurence Date and Report Date into a proper date because 
Date Time is easier to work with.

'''
bike_df['Occurrence_Date'] = pd.to_datetime(bike_df['Occurrence_Date'])
bike_df['Occurrence_Date'] = bike_df['Occurrence_Date'].dt.date
bike_df['Occurrence_Date'] = bike_df['Occurrence_Date'].astype('datetime64')

bike_df['Report_Date'] = pd.to_datetime(bike_df['Report_Date'])
bike_df['Report_Date'] = bike_df['Report_Date'].dt.date
bike_df['Report_Date'] = bike_df['Report_Date'].astype('datetime64')
print(bike_df.dtypes) 
'''
Now we deal with the columns with missing values.

Bike Make Values that are missing are currently logged as NaN. This should be replaced with Unknown Make.
Bike Model values that are logged as NaN should also be replaced with Unknown Model.
Replace NaN in Bike_Colour with "Unknown Colour"
For the Cost of Bike,we shoudl replace NaN with the average cost of a bike. 0's should be find in this scenario because
bikes can have 0 cost (eg.gifts or value of bike cannot be calcualted).
'''

bike_df['Bike_Make'] = bike_df['Bike_Make'].fillna('Unknown Make')

bike_df['Bike_Model'] = bike_df['Bike_Model'].fillna('Unknown Model')
bike_df['Bike_Colour'] = bike_df['Bike_Colour'].fillna('Unknown Colour')

bike_df['Cost_of_Bike'] = bike_df['Cost_of_Bike'].fillna(bike_df['Cost_of_Bike'].mean())

print("# of Null Values: \n")
print(bike_df.isnull().sum())

'''
The initial Data is cleaned up, we can save a copy of this as step 1. In step 2, we determine if there are any outliers 
in the data set and can be removed.
'''
bike_df.to_csv('.\data\Bicycle_Thefts_CleanStep1.csv')

