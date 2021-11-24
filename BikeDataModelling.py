# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:31:42 2021

@author: asjya

Preform comparitive analysis and modelling
"""

import pandas as pd
import matplotlib.pyplot as plt
import math
import os

path = ".\data"
filename = 'Bicycle_Thefts_CleanStep1.csv'
fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)


'''
The feature we will be targeting is the status of the bike. All bikes are stolen in this data set so we cannot do a 
predicition on the likeliness of a bike being stolen. We can however predict if a stolen bike is likly to be recovered.

The target variable is status. Ignore column 1 as thats just the row # column.
We now need to find the correlation the various varibales and our target variable.

I  Have decided to use a Decision Tree Classifier to determine which state it will end up being (Stolen, Returned,)
'''

# Splitting the predictor and target variables 
colnames=bike_df.columns.values.tolist()
print(colnames)

predictors=colnames[:4]
'''
from sklearn.tree import DecisionTreeClassifier
dt_alvin = DecisionTreeClassifier(criterion='entropy',min_samples_split=20, random_state=99)
dt_alvin.fit(train[predictors], train[target])

preds=dt_alvin.predict(test[predictors])
print(pd.crosstab(test['Species'],preds,rownames=['Actual'],colnames=['Predictions']))

from sklearn.tree import export_graphviz
with open('D:/School/Fall 2021/Data Warehousing/dtree2.dot', 'w') as dotfile:
   export_graphviz(dt_alvin, out_file = dotfile, feature_names = predictors)

dotfile.close()
'''


#target=colnames[4]
#print('Target:'+target)
