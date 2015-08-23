__author__ = 'Justin'
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier


def tree(titanic):
    predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

    # Initialize the  algorithm with the default paramters
    # n_estimators is the number of trees we want to make
    # min_samples_split is the minimum number of rows we need to make a split
    # min_samples_leaf is the minimum number of samples we can have at the place where a tree branch ends (the bottom points of the tree)
    alg = RandomForestClassifier(random_state=1, n_estimators=500, min_samples_split=4, min_samples_leaf=2)
    scores = cross_validation.cross_val_score(alg,titanic[predictors],titanic["Survived"],cv = 3)
    return (scores.mean())