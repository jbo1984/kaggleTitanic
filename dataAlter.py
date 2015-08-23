__author__ = 'Justin Bollinger'

def dataMani(titanic):

    # print(titanic.head(5))
    # print(titanic.describe())
    #Makes blank ages the median age.
    titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())


    #print(titanic["Sex"].unique())
    #converts sex's to 0 and 1
    titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
    titanic.loc[titanic["Sex"] == 'female', "Sex"] = 1

    #print(titanic["Embarked"].unique())
    #Made n/a S which is the most common port. Converted ports to numbers.
    titanic["Embarked"] = titanic["Embarked"].fillna("S")
    titanic.loc[titanic["Embarked"] == 'S', "Embarked"] = 0
    titanic.loc[titanic["Embarked"] == 'C', "Embarked"] = 1
    titanic.loc[titanic["Embarked"] == 'Q', "Embarked"] = 2

    titanic["Fare"] = titanic["Fare"].fillna(titanic["Fare"].median)

    titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]
    titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))


    return titanic