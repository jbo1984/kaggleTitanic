__author__ = 'Justin'
import pandas as pd
import pylab as p
import numpy as np
import linearMachine, dataAlter
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier



# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("train.csv")
dataAlter.dataMani(titanic)
#print(titanic)
pred = linearMachine.regModel(titanic)
pred = np.concatenate(pred, 0)

pred[pred > .5] = 1
pred[pred <= .5] = 0
#print(pred)

count = 0
accuracy = 0
while count < len(titanic["Survived"]):

    if titanic["Survived"][count] == pred[count]:
        accuracy += 1
    count += 1

accuracy = accuracy / float(len(titanic))
print accuracy
# submission = pd.DataFrame({
#         "PassengerId": titanic["PassengerId"],
#         "Survived": pred
#     })
# submission = pd.DataFrame
# submission.to_csv("submission.csv")


predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

# Initialize our algorithm with the default paramters
# n_estimators is the number of trees we want to make
# min_samples_split is the minimum number of rows we need to make a split
# min_samples_leaf is the minimum number of samples we can have at the place where a tree branch ends (the bottom points of the tree)
alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)
scores = cross_validation.cross_val_score(alg,titanic[predictors],titanic["Survived"],cv = 3)
print(scores.mean())