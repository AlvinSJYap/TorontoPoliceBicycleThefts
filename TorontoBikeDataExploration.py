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
18 Columns are of mixed data types which we will need to handle.
Bike_Make, Bike_Model, Bike_Colour, and Cost_of_Bike have numerous null values that we need to handle.
''' 

print('\n Mode of Categorical Columns: \n')
print(bike_df[bike_df.select_dtypes(include=['object']).columns.tolist()].mode())

'''
Lets see which the yearly counts of how mnay thefts. Convert the Obejct Data type of the Occurence Date into a proper date 
time

'''








