# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 00:59:29 2021

@author: Alvin Yap
"""

import pandas as pd
import matplotlib.pyplot as plt
import math
import os
import seaborn as sns

def printSeparator(value):
  print('\n' * 4)
  print(value)
  print('\n')

plt.close("all")
path = ".\data"
filename = 'Bicycle_Thefts.csv'
fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)

printSeparator(' RAW CSV ')
print(bike_df)

pd.set_option('display.max_columns',15)

printSeparator('bike_df.head():')
print(bike_df.head())

printSeparator('bike_df.columns.values:')
print(bike_df.columns.values)

printSeparator('bike_df.shape:')
print(bike_df.shape)

printSeparator('bike_df.describe():')
print(bike_df.describe())

printSeparator('bike_df.dtypes:')
print(bike_df.dtypes)

printSeparator('bike_df.head(5):')
print(bike_df.head(5))

printSeparator('# of Null Values:')
print(bike_df.isnull().sum())


printSeparator('Mean of Numerical Columns:')
print(bike_df.mean())
'''
There are 35 columns and 25569 rows in the bike dataframe.
2 Columns should be datetime but are coming out as string. We can clean this up
Bike_Make, Bike_Model, Bike_Colour, and Cost_of_Bike have numerous null values that we need to handle.
'''

printSeparator('Mode of Categorical Columns:')
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

printSeparator("# of Null Values:")
print(bike_df.isnull().sum())


'''
The feature we will be targeting is the status of the bike. All bikes are stolen in this data set so we cannot do a 
predicition on the likeliness of a bike being stolen. We can however predict if a stolen bike is likly to be recovered.
One interesting data point that is not immediately available in this data set is the time between report and occurrence.

We will add this column as Report Lag

'''

bike_df['Report_Lag'] = bike_df['Report_Date'] - bike_df['Occurrence_Date']
printSeparator('bike_df.Report_Lag:')
print(bike_df['Report_Lag'])

'''
Looking at status, we have 3 categories, however the 3rd category is unknown. This does not help us
in any case for our prediction since it inidicates that there was no colncusion (no follow up on if the bike was
                                                                                 found or not).

Get the row #'s that contain unknown and remove them
'''

#These are the rows that contain unknown in the status column.

dropped_rows = bike_df[ bike_df['Status'] == 'UNKNOWN'].index

print(dropped_rows)

bike_df = bike_df.drop(dropped_rows)

bike_df.reset_index()

print(bike_df)

#Don't need event_unique_id
bike_df = bike_df.drop('event_unique_id', 1)

#Don't need X
bike_df = bike_df.drop('X', 1)

#Don't need Y
bike_df = bike_df.drop('Y', 1)

#Hot encode the rest of the categorical data
'''
The initial Data is cleaned up, we can save a copy of this as step 1. In step 2, we determine if there are any outliers
in the data set and can be removed.
'''

bike_df.to_csv('.\data\Bicycle_Thefts_CleanStep1.csv')


'''
Cleanup bike cost values
'''
bike_df['Cost_of_Bike'] = bike_df['Cost_of_Bike'].round()

maxPrice = bike_df['Cost_of_Bike'].max()

fig, ax = plt.subplots(3, constrained_layout=True)

sns.boxplot(x='Cost_of_Bike', data=bike_df, ax=ax[0]).set(xlabel='', title='Cost of Bike With Outliers'),;

# remove outliers
q1 = bike_df["Cost_of_Bike"].quantile(0.25)
q3 = bike_df["Cost_of_Bike"].quantile(0.75)

df_no_outliers = bike_df.loc[(bike_df["Cost_of_Bike"] > q1) & (bike_df["Cost_of_Bike"] < q3)]

print(q3)

print('Most expensive bike', maxPrice)



'''
Plotting with no outliers
'''
test_plot_x = df_no_outliers['Cost_of_Bike']
test_plot_y = df_no_outliers['Status'].apply(lambda x: 0 if x == 'STOLEN' else 1)

sns.boxplot(x='Cost_of_Bike', data=df_no_outliers, ax=ax[1]).set(xlabel='', title='Cost of Bike No Outliers'),

'''
Pie Chart of stolen vs recovered
'''
stolenCount = bike_df[bike_df['Status'] == 'STOLEN']['Status'].count()
recoveredCount = bike_df[bike_df['Status'] == 'RECOVERED']['Status'].count()

labels = 'Stolen', 'Recovered'

ax[2].pie([stolenCount, recoveredCount], labels=labels, autopct='%1.1f%%')



plt.show()