# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:31:42 2021

@author: asjya

Preform Data cleaning on the Categorical Columns. The goal of this is to reduce the amount of 
categorical data that needs to become dummy variables Ultimately if we can turn a categorical column in to
a binary, that would be ideal otherwise we will have to oneHotEncode.
"""

import pandas as pd


import os

def printSeparator(value):
  print('\n' * 4)
  print(value)
  print('\n')
  
  
path = ".\data"
filename = 'Bicycle_Thefts_CleanStep1.csv'
fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)

cat_bike_df = bike_df.select_dtypes(include=['object']).copy()

printSeparator(' Unique Values ')
print(cat_bike_df.nunique())

printSeparator(' Unique Values in Primary Offence:Before ')
print(pd.unique(cat_bike_df['Primary_Offence'].values))

'''
In order to make this column more manageable, we will relabel the unique values and group many of them under
a similar category. This one will be one hot encoded.

Categories:
    1.Theft
    2.B&E
    3.Mischief
    4.FTC
    5.Robbery
    6.Trafficking
    7.Property
    8.Assault
    9.Fraud
    10.Drug
    11.Property (possesion of property obtained by crime)
    12.Weapon
    13.Other
'''
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('theft', case=False),'Primary_Offence'] = 'THEFT'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('break', case=False),'Primary_Offence'] = 'B&E'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('trespass', case=False),'Primary_Offence'] = 'ASSAULT'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('b&e', case=False),'Primary_Offence'] = 'B&E'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('mischief', case=False),'Primary_Offence'] = 'MISCHIEF'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('ftc', case=False),'Primary_Offence'] = 'FTC'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('trafficking', case=False),'Primary_Offence'] = 'TRAFFICKING'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('robbery', case=False),'Primary_Offence'] = 'ROBBERY'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('threat', case=False),'Primary_Offence'] = 'ASSAULT'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('assault', case=False),'Primary_Offence'] = 'ASSAULT'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('aslt', case=False),'Primary_Offence'] = 'ASSAULT'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('fraud', case=False),'Primary_Offence'] = 'FRAUD'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('property', case=False),'Primary_Offence'] = 'PROPERTY'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('drug', case=False),'Primary_Offence'] = 'DRUG'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('weapon', case=False),'Primary_Offence'] = 'WEAPON'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('liquor', case=False),'Primary_Offence'] = 'DRUG'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('RMS', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('fire', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('other', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('suspicious', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('unlawfully', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('information', case=False),'Primary_Offence'] = 'OTHER'
cat_bike_df.loc[cat_bike_df['Primary_Offence'].str.contains('arr', case=False),'Primary_Offence'] = 'OTHER'

printSeparator(' Unique Values in Primary Offence: After ')
print(pd.unique(cat_bike_df['Primary_Offence'].values))



'''
Next up is Occurrence Date. Realistically, the date itself is not important.We can drop this column, as any
meaningfull  analysis can be done on powerBI. The same can be said for report date as the key data we extract from 
this is the lag in Occurrence to report.
'''

cat_bike_df = cat_bike_df.drop('Occurrence_Date', 1)
cat_bike_df = cat_bike_df.drop('Report_Date', 1)
printSeparator(' Unique Values after Occurrence Date and Report Date Dropped')
print(cat_bike_df.nunique())

'''
Occurrence / Report Month and Day of week. Both of these can be easily converted to 1-12 to indicate the month, and
1-7 to indicate the day of the week.
'''

cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('monday', case=False),'Occurrence_DayOfWeek'] = '1'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('tuesday', case=False),'Occurrence_DayOfWeek'] = '2'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('wednesday', case=False),'Occurrence_DayOfWeek'] = '3'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('thursday', case=False),'Occurrence_DayOfWeek'] = '4'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('friday', case=False),'Occurrence_DayOfWeek'] = '5'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('saturday', case=False),'Occurrence_DayOfWeek'] = '6'
cat_bike_df.loc[cat_bike_df['Occurrence_DayOfWeek'].str.contains('sunday', case=False),'Occurrence_DayOfWeek'] = '7'
cat_bike_df['Occurrence_DayOfWeek']= cat_bike_df['Occurrence_DayOfWeek'].astype('int32')

cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('monday', case=False),'Report_DayOfWeek'] = '1'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('tuesday', case=False),'Report_DayOfWeek'] = '2'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('wednesday', case=False),'Report_DayOfWeek'] = '3'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('thursday', case=False),'Report_DayOfWeek'] = '4'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('friday', case=False),'Report_DayOfWeek'] = '5'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('saturday', case=False),'Report_DayOfWeek'] = '6'
cat_bike_df.loc[cat_bike_df['Report_DayOfWeek'].str.contains('sunday', case=False),'Report_DayOfWeek'] = '7'
cat_bike_df['Report_DayOfWeek']= cat_bike_df['Report_DayOfWeek'].astype('int32')


cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('jan', case=False),'Occurrence_Month'] = '1'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('feb', case=False),'Occurrence_Month'] = '2'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('mar', case=False),'Occurrence_Month'] = '3'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('apr', case=False),'Occurrence_Month'] = '4'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('may', case=False),'Occurrence_Month'] = '5'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('jun', case=False),'Occurrence_Month'] = '6'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('jul', case=False),'Occurrence_Month'] = '7'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('aug', case=False),'Occurrence_Month'] = '8'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('sep', case=False),'Occurrence_Month'] = '9'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('oct', case=False),'Occurrence_Month'] = '10'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('nov', case=False),'Occurrence_Month'] = '11'
cat_bike_df.loc[cat_bike_df['Occurrence_Month'].str.contains('dec', case=False),'Occurrence_Month'] = '12'
cat_bike_df['Occurrence_Month']= cat_bike_df['Occurrence_Month'].astype('int32')

cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('jan', case=False),'Report_Month'] = '1'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('feb', case=False),'Report_Month'] = '2'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('mar', case=False),'Report_Month'] = '3'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('apr', case=False),'Report_Month'] = '4'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('may', case=False),'Report_Month'] = '5'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('jun', case=False),'Report_Month'] = '6'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('jul', case=False),'Report_Month'] = '7'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('aug', case=False),'Report_Month'] = '8'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('sep', case=False),'Report_Month'] = '9'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('oct', case=False),'Report_Month'] = '10'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('nov', case=False),'Report_Month'] = '11'
cat_bike_df.loc[cat_bike_df['Report_Month'].str.contains('dec', case=False),'Report_Month'] = '12'

cat_bike_df['Report_Month']= cat_bike_df['Report_Month'].astype('int32')
printSeparator(' Occurence and Report Days/Months Coded')
print(pd.unique(cat_bike_df['Occurrence_DayOfWeek'].values))
print(pd.unique(cat_bike_df['Occurrence_Month'].values))

'''
Division is neatly set up where we can just remove the D from the value. NSA can be converted to either 0 or -1.
'''
printSeparator(' Unique Values in Divison: Before')
print(pd.unique(cat_bike_df['Division'].values))


cat_bike_df.loc[cat_bike_df['Division'].str.contains('NSA',case=False),'Division'] = 'D0'
cat_bike_df['Division'] = cat_bike_df['Division'].str[1:]
cat_bike_df['Division']= cat_bike_df['Division'].astype('int32')
printSeparator(' Unique Values in Divison: After')
print(pd.unique(cat_bike_df['Division'].values))
print(cat_bike_df.dtypes)


'''

City is binary, we can have toronto be 1, and NSA =0 


'''

printSeparator(' Unique Values in City')
print(pd.unique(cat_bike_df['City'].values))
cat_bike_df.loc[cat_bike_df['City'].str.contains('tor', case=False),'City'] = '1'
cat_bike_df.loc[cat_bike_df['City'].str.contains('nsa', case=False),'City'] = '0'
cat_bike_df['City']= cat_bike_df['City'].astype('int32')


'''
HoodId: This is a mixed data type because of the NSA and some ints being strings. We will replace it with a value of 0. 
We will convert all the values into strings and then back into integerrs
'''

printSeparator(' Unique Values in Hood_id')
cat_bike_df['Hood_ID'] = cat_bike_df['Hood_ID'].astype(str)
cat_bike_df.loc[cat_bike_df['Hood_ID'].str.contains('nsa', case=False),'Hood_ID'] = '0'

print(pd.unique(cat_bike_df['Hood_ID'].values))
cat_bike_df['Hood_ID']= cat_bike_df['Hood_ID'].astype('int32')
print(cat_bike_df.dtypes)

'''
NeighbourhoodName:
We can drop this column because it's just the string value of hood_ID, we can match it later

'''
printSeparator(' Unique Values in Neighbourhood Name')
print(pd.unique(cat_bike_df['NeighbourhoodName'].values))
cat_bike_df = cat_bike_df.drop('NeighbourhoodName', 1)

'''
Location_Type

go from 42 location types to 10.


'''

printSeparator(' Unique Values in Location_Type : Before')
#print(pd.unique(cat_bike_df['Location_Type'].values))
print(cat_bike_df['Location_Type'].value_counts())
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('ttc', case=False),'Location_Type'] = 'Public Transit Hub'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('go', case=False),'Location_Type'] = 'Public Transit Hub'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('transit', case=False),'Location_Type'] = 'Public Transit Hub'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('train', case=False),'Location_Type'] = 'Public Transit Hub'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('Non-Profit', case=False),'Location_Type'] = 'Non-Commerical/Public Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('religious', case=False),'Location_Type'] = 'Non-Commerical/Public Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('schools', case=False),'Location_Type'] = 'Non-Commerical/Public Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('For Profit', case=False),'Location_Type'] = 'Commericial / Corporate Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('bank', case=False),'Location_Type'] = 'Commericial / Corporate Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('hotel', case=False),'Location_Type'] = 'Commericial / Corporate Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('dealership', case=False),'Location_Type'] = 'Commericial / Corporate Areas'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('medical', case=False),'Location_Type'] = 'Medical Facilities'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('pharmacy', case=False),'Location_Type'] = 'Medical Facilities'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('jail', case=False),'Location_Type'] = 'Corrections Facilities'
cat_bike_df.loc[cat_bike_df['Location_Type'].str.contains('police', case=False),'Location_Type'] = 'Corrections Facilities'

printSeparator(' Unique Values in Location_Type : After')
print(cat_bike_df['Location_Type'].value_counts())


'''
Premises_Type: These are already nicely grouped, can be easily oneHotEncoded.

'''
printSeparator(' Unique Values in Premises_Type')
print(cat_bike_df['Premises_Type'].value_counts())

'''
Bike_Model: A majority a large subset of this column is unknown. We can safely drop this column from the model
as it provides us with no meanifull information. 40% of the models are unknown. No other Model
makes up for more than 0.5% of the missing bikes 

'''

printSeparator(' Unique Values in Bike_Model')
print(cat_bike_df['Bike_Model'].value_counts(normalize=True).head())

#print(pd.unique(cat_bike_df['Bike_Make'].values))
cat_bike_df = cat_bike_df.drop(['Bike_Model'], axis=1)



'''

Bike_Type: This column is suitable for oneHotencoding and does not need to be regrouped.
'''
printSeparator(' Unique Values in Bike_Type')
print(cat_bike_df['Bike_Type'].value_counts())


'''
Bike_Colour: group up everything that is under LBL together as OTHER.

'''


printSeparator(' Unique Values in Bike_Colour : Before')
print(cat_bike_df['Bike_Colour'].value_counts())
print(cat_bike_df['Bike_Colour'].value_counts(normalize=True).head(20))

allowed_vals = ['BLK','BLU','GRY','Unknown Colour','WHI','RED','SIL','GRN','ONG','PLE','DBL','YEL','LBL']
cat_bike_df.loc[~cat_bike_df['Bike_Colour'].isin(allowed_vals), "Bike_Colour"] = "Other"
printSeparator(' Unique Values in Bike_Colour : After')
print(cat_bike_df['Bike_Colour'].value_counts(normalize=True))


'''
Report Lag: substring the first value since thats the numerical value we want.

'''

printSeparator(' Unique Values in Report Lag: Before')
print(cat_bike_df['Report_Lag'].value_counts())


cat_bike_df['Report_Lag'] = cat_bike_df['Report_Lag'].str[:-4]
cat_bike_df['Report_Lag'] = cat_bike_df['Report_Lag'].astype('int32')
print(cat_bike_df['Report_Lag'].value_counts())


'''
Bike_Make: The way the data is disrubuted, i believe that this column has very little to offer in terms 
determining if a bike is to be returned. The cardinality is to high, and there seems to be very little correlation.

'''
printSeparator(' Unique Values in Bike_Make')
print(cat_bike_df['Bike_Make'].value_counts(normalize=True).head(20))
cat_bike_df = cat_bike_df.drop(['Bike_Make'], axis=1)
print(cat_bike_df.dtypes)
print(cat_bike_df.nunique())

#replace the values from the old dataframe with those after we cleaned
bike_df.loc[:, ['Primary_Offence','Occurrence_Month','Occurrence_DayOfWeek','Report_Month','Report_DayOfWeek','Division','City','Hood_ID','Location_Type','Premises_Type','Bike_Type','Bike_Colour','Status','Report_Lag']] = cat_bike_df[['Primary_Offence','Occurrence_Month','Occurrence_DayOfWeek','Report_Month','Report_DayOfWeek','Division','City','Hood_ID','Location_Type','Premises_Type','Bike_Type','Bike_Colour','Status','Report_Lag']]


'''

Remove columns from this data set that do not help the model
'''
bike_df = bike_df.drop('Occurrence_Date', 1)
bike_df = bike_df.drop('Report_Date', 1)
bike_df = bike_df.drop(['Bike_Make'], axis=1)
bike_df = bike_df.drop('NeighbourhoodName', 1)
bike_df = bike_df.drop(['Bike_Model'], axis=1)
bike_df = bike_df.drop(['ObjectId2'], axis=1)
bike_df = bike_df.drop(['Longitude'], axis=1)
bike_df = bike_df.drop(['Latitude'], axis=1)
bike_df = bike_df.drop(['Unnamed: 0'], axis=1)
#bike_df = bike_df.drop(['X'], axis=1)
#bike_df = bike_df.drop(['Y'], axis=1)
bike_df = bike_df.drop(['OBJECTID'], axis=1)

bike_df.to_csv('.\data\Bicycle_Thefts_CleanStep2.csv')