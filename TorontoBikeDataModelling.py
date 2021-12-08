# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 06:11:34 2021

@author: asjya

create a model 
"""

import pandas as pd
import os

path = os.path.dirname(os.path.realpath(__file__))
filename = 'data\\Bicycle_Thefts_CleanStep3.csv'

fullpath = os.path.join(path,filename)
bike_df = pd.read_csv(fullpath)
bike_df = bike_df.iloc[: , 1:]


colnames=bike_df.columns.values.tolist()
colnames.remove('Status')


from sklearn.tree import DecisionTreeClassifier


import numpy as np

X=bike_df[colnames]
Y=bike_df['Status']
#split the data sklearn module
from sklearn.model_selection import train_test_split
trainX,testX,trainY,testY = train_test_split(X,Y, test_size = 0.2)




dt_bike= DecisionTreeClassifier(criterion='entropy',max_depth=10, min_samples_split=20, random_state=99)
dt_bike.fit(trainX,trainY)
# 10 fold cross validation using sklearn and all the data i.e validate the data 
from sklearn.model_selection import KFold
#help(KFold)
crossvalidation = KFold(n_splits=10, shuffle=True, random_state=1)
from sklearn.model_selection import cross_val_score
score = np.mean(cross_val_score(dt_bike, trainX, trainY, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print(score)

# Feature 21, 11 are important for prediction, while feature 2, 7 are 
# important but far less important 
#### Get feature importance
from matplotlib import pyplot
importance = dt_bike.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
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
with open(os.path.join(path,'data\\dtree2.dot'), 'w') as dotfile:
   export_graphviz(dt_bike, out_file = dotfile, feature_names = colnames)

dotfile.close()
'''
import pickle

filename = 'pickledBikeModel'
outfile = open(filename,'wb')

pickle.dump(dt_bike,outfile)
outfile.close()

'''