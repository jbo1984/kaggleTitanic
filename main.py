__author__ = 'Justin Bollinger'
import pandas as pd, numpy as np
import linearMachine, dataAlter, randomTree, bestSelector




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

tree = randomTree.tree(titanic)
# print(titanic)
# titanic = pd.DataFrame(titanic)
# titanic.to_csv("submission.csv")

print(bestSelector.bSelect(titanic))
print(randomTree.tree(titanic))