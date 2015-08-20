__author__ = 'Justin Bollinger'

from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold



def regModel(titanic):
    predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


    alg = LinearRegression()
    kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

    predictions = []
    for train, test in kf:
        train_predictors = (titanic[predictors].iloc[train,:])
        train_target = titanic["Survived"].iloc[train]
        alg.fit(train_predictors, train_target)
        test_predictions = alg.predict(titanic[predictors].iloc[test,:])
        predictions.append(test_predictions)

    return predictions