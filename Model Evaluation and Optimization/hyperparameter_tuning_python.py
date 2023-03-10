# -*- coding: utf-8 -*-
"""Hyperparameter Tuning - Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hzUMrxKuBSZiVeQ9vlYQPD-4fdOq0lCI

#Import the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
import sklearn.datasets
from sklearn.svm import SVC

"""#Data Collection and preprocessing"""

bc_ds = sklearn.datasets.load_breast_cancer()

print(bc_ds)

bc_data = pd.DataFrame(bc_ds.data,columns=bc_ds.feature_names)
bc_data.head()

bc_data['label'] = bc_ds.target

bc_data.shape

bc_data.isnull().sum()

bc_data['label'].value_counts()

"""#Splitting features and label"""

X = bc_data.drop(columns='label',axis=1)
Y = bc_data['label']

X = np.asarray(X)
Y = np.asarray(Y)

"""#Grid Search CV"""

model = SVC()

#hyperparameters

parameters={'kernel':['linear','poly','rbf','sigmoid'],'C':[1,5,10,20]}

classifier = GridSearchCV(model,parameters,cv=5)

classifier.fit(X,Y)

#Best parameter
best_p = classifier.best_params_
print(best_p)

#highest accuracy
high_acc = classifier.best_score_
print(round(high_acc*100,2))

result = pd.DataFrame(classifier.cv_results_)
result.head()

grid_search_result = result[['param_C','param_kernel','mean_test_score']]
grid_search_result

"""#Randomized Search CV"""

model = SVC()

#hyperparameters

parameters={'kernel':['linear','poly','rbf','sigmoid'],'C':[1,5,10,20]}

classifier = RandomizedSearchCV(model,parameters,cv=5)

classifier.fit(X,Y)

#Best parameter
best_p = classifier.best_params_
print(best_p)

#highest accuracy
high_acc = classifier.best_score_
print(round(high_acc*100,2))

result = pd.DataFrame(classifier.cv_results_)
result.head()

randomized_search_result = result[['param_C','param_kernel','mean_test_score']]
randomized_search_result

