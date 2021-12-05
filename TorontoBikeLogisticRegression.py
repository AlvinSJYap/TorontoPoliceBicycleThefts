import pandas as pd
import numpy as np
import os

model_export_path = 'data\\models\\logistic\\'
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

from sklearn.linear_model import LogisticRegression
dependent_variable = 'Status'

# Another way to split the features
x = scaled_df[scaled_df.columns.difference([dependent_variable])]
x.dtypes
y = scaled_df[dependent_variable]

#convert the class back into integer
y = y.astype(int)

# Split the data into train test
from sklearn.model_selection import train_test_split
trainX,testX,trainY,testY = train_test_split(x,y, test_size = 0.2)

#build the model
lr = LogisticRegression(solver='liblinear')
lr.fit(x, y)

# Score the model using 10 fold cross validation
from sklearn.model_selection import KFold
crossvalidation = KFold(n_splits=10, shuffle=True, random_state=1)
from sklearn.model_selection import cross_val_score
score = np.mean(cross_val_score(lr, trainX, trainY, scoring='accuracy', cv=crossvalidation, n_jobs=1))
print ('The score of the 10 fold run is: ',score)

testY_predict = lr.predict(testX)
testY_predict.dtype

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
labels = y.unique()

print(labels)
print("Accuracy:", metrics.accuracy_score(testY, testY_predict))

#Let us print the confusion matrix
from sklearn.metrics import confusion_matrix
print("Confusion matrix \n" , confusion_matrix(testY, testY_predict, labels))

import joblib
joblib.dump(lr, os.path.join(path, model_export_path, 'model_lr2.pkl'))
print("Model dumped!")

model_columns = list(x.columns)
joblib.dump(model_columns, os.path.join(path, model_export_path, 'model_columns.pkl'))
print("Models columns dumped!")