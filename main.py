__author__ = 'Justin'
import pandas as pd
import linearMachine, dataAlter



# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("train.csv")
dataAlter.dstaMani(titanic)
#print(titanic)
pred = linearMachine.regModel(titanic)
print(pred)

