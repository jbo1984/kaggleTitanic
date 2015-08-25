__author__ = 'Justin'
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from matplotlib import pyplot as plt


def bSelect(titanic):
    predictors = ["Pclass","Sex","Age","SibSp","Parch","Fare","Embarked","FamilySize","Title","FamilyId"]
    #Preforms feature selection
    selector = SelectKBest(f_classif, k = 5)
    selector.fit(titanic[predictors], titanic["Survived"])

    #Gets the raw p values for each feature and and transforms to scores
    scores = -np.log10(selector.pvalues_)
    #PLot of scores
    plt.bar(range(len(predictors)), scores)
    plt.xticks(range(len(predictors)), predictors, rotation='vertical')
    plt.show()

    predictors = ["Pclass", "Sex", "Fare", "Title"]

    alg = RandomForestClassifier(random_state=1, n_estimators=150, min_samples_split=8, min_samples_leaf=4)
    scores = cross_validation.cross_val_score(alg,titanic[predictors],titanic["Survived"],cv = 3)
    return (scores.mean())