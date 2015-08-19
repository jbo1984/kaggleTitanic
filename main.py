__author__ = 'Justin'
import pandas as pd
import linearMachine



# This creates a pandas dataframe and assigns it to the titanic variable. file_select is to select train.csv
titanic = pd.read_csv("train.csv")

# print(titanic.head(5))
# print(titanic.describe())
#Makes blank ages the median age
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
print(titanic)


