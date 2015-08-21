__author__ = 'Justin'
import pandas as pd
import pylab as p
import numpy as np
import linearMachine, dataAlter




# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("train.csv")
dataAlter.dstaMani(titanic)
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
print(accuracy)

