# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 06:11:34 2021

@author: asjya

create a model 
"""

import pandas as pd
import os
from matplotlib import pyplot


import os
path = "data"
filename = 'Bicycle_Thefts_CleanStep3.csv'
fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)
bike_df = bike_df.iloc[: , 1:]

def printSeparator(value):
  print('\n' * 4)
  print(value)
  print('\n')
colnames=bike_df.columns.values.tolist()
colnames.remove('Status')


from sklearn.tree import DecisionTreeClassifier


import numpy as np

X=bike_df[colnames]
Y=bike_df['Status']




#split the data sklearn module
from sklearn.model_selection import train_test_split
trainX,testX,trainY,testY = train_test_split(X,Y, test_size = 0.2)






'''
Sample the data , and use this as the new training data
'''

from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(trainX, trainY)


printSeparator('Y-Resample BiCount')
print(np.bincount(y_res))

printSeparator('X-Resample')
print(X_res)


'''
Sklearn feature selection

'''

printSeparator('Column Names')
print(colnames)

printSeparator('Feature Selection')
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
fs = SelectKBest(score_func=chi2, k='all')
fs.fit(X_res,y_res)

# what are scores for the features
for i in range(len(fs.scores_)):
	print('Feature %d: %f' % (i, fs.scores_[i]))
# plot the scores
sortedArray= sorted(fs.scores_,reverse=True)

pyplot.bar([i for i in range(len(fs.scores_))],sortedArray)
pyplot.show()

'''
Based off the plot, i want to take the top 75 features.
'''
fs2 = SelectKBest(score_func=chi2, k=75)
fs2.fit(X_res,y_res)
# get the indices for the target columns
targetCols =fs2.get_support(indices=True)
print(targetCols)


#update X to only include these new columns from the dataframe

X=bike_df.iloc[:,targetCols]
print(X)




print(sortedArray)
dt_bike= DecisionTreeClassifier(criterion='entropy',max_depth=8, min_samples_split=20, random_state=99)
dt_bike.fit(X_res,y_res)
# 10 fold cross validation using sklearn and all the data i.e validate the data 
from sklearn.model_selection import KFold
#help(KFold)
crossvalidation = KFold(n_splits=10, shuffle=True, random_state=1)
from sklearn.model_selection import cross_val_score
score = np.mean(cross_val_score(dt_bike, X_res, y_res, scoring='accuracy', cv=crossvalidation, n_jobs=1))
#print(score)

# Feature 21, 11 are important for prediction, while feature 2, 7 are 
# important but far less important 
#### Get feature importance

importance = dt_bike.feature_importances_
# summarize feature importance
#for i,v in enumerate(importance):
#	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.show()


### Test the model using the testing data
testY_predict = dt_bike.predict(testX)

testY_predict.dtype
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics 
labels = Y.unique()
print(labels)
print("Accuracy:",metrics.accuracy_score(testY, testY_predict))
#Let us print the confusion matrix
from sklearn.metrics import confusion_matrix
print("Confusion matrix \n" , confusion_matrix(testY, testY_predict, labels))


import seaborn as sns
import matplotlib.pyplot as plt     
cm = confusion_matrix(testY, testY_predict, labels)
ax= plt.subplot()
sns.heatmap(cm, annot=True, ax = ax); #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix'); 
ax.xaxis.set_ticklabels(['Stolen','Recovered']); ax.yaxis.set_ticklabels(['Stolen','Recovered']);
plt.show()
from sklearn import tree
tree.plot_tree(dt_bike)
from sklearn.tree import export_graphviz
#with open('D:/School/Fall 2021/Data Warehousing/GroupProject/TorontoPoliceBicycleThefts/data/dtree2.dot', 'w') as dotfile:
with open('./data/dtree2.dot', 'w') as dotfile:

   export_graphviz(dt_bike, out_file = dotfile, feature_names = colnames)

dotfile.close()
'''
import pickle

filename = 'pickledBikeModel'
outfile = open(filename,'wb')

pickle.dump(dt_bike,outfile)
outfile.close()

'''

