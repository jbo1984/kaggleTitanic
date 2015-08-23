__author__ = 'Justin Bollinger'
import pandas as pd
import re, operator
# A dictionary mapping family name to id
family_id_mapping = {}

def get_title(name):

    #Reg exp to search for name titles ex Mr. Mrs.
    title_search = re.search(' ([A-Za-z]+)\.', name)
    #Extract title if it exists
    if title_search:
        return title_search.group(1)
    return ""

def get_family_id(titanic):
    # Find the last name by splitting on a comma
    last_name = titanic["Name"].split(",")[0]
    # Create the family id
    family_id = "{0}{1}".format(last_name, titanic["FamilySize"])
    # Look up the id in the mapping
    if family_id not in family_id_mapping:
        if len(family_id_mapping) == 0:
            current_id = 1
        else:
            # Get the maximum id from the mapping and add one to it if no id
            current_id = (max(family_id_mapping.items(), key=operator.itemgetter(1))[1] + 1)
        family_id_mapping[family_id] = current_id
    return family_id_mapping[family_id]

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

    #gets each title
    titles = titanic["Name"].apply(get_title)
    #print(pd.value_counts(titles))

    #Maps titles to integer
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7,
                     "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10,
                     "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
    for k,v in title_mapping.items():
        titles[titles == k] = v
    #print(pd.value_counts(titles))
    titanic["Title"] = titles

    #gets family ids
    family_ids = titanic.apply(get_family_id, axis=1)
    family_ids[titanic["FamilySize"] < 3] = -1
    titanic["FamilyId"] = family_ids
    #print(pd.value_counts(family_ids))

    return titanic