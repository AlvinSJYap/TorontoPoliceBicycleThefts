import pandas as pd
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))
filename = 'data\Bicycle_Thefts_CleanStep3.csv'
fullpath = os.path.join(path,filename)

pd.set_option('display.max_columns',30) # set the maximum width
# Load the dataset in a dataframe object
df = pd.read_csv(fullpath)


from sklearn import preprocessing

# Get column names first
names = df.columns

# Create the Scaler object
scaler = preprocessing.StandardScaler()

# Fit your data on the scaler object
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns=names)
print(scaled_df.head())
print(scaled_df.dtypes)