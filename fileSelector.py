__author__ = 'Justin'
#This allows for selection of csv's being used
from Tkinter import *
import tkFileDialog

def file_select():
    master = Tk()
    master.withdraw() #hiding tkinter window
    file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("csv file",".csv"),("All files",".*")])

    master.quit()