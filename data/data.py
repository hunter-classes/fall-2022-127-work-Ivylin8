#1 extra: Use Matplotlib or another Python graphing/plotting library to visualize part or all of your analysis.

#NOTE: Used Jupiter Notebook from Anaconda 


#import data using csv
import csv
import numpy

with open('general_rates.csv')as csvfile:
    for i in csv.reader(csvfile):
        print(','.join(i))
    print('')


#extra
from matplotlib import pyplot as plt
#set up x and y axis
x = [2005, 2006, 2007, 2008, 2009]
y = [13, 14, 15, 16, 17]
#input data and label
plt.scatter(x, y)
plt.title("General Rates")
plt.xlabel("Count (rate)")
plt.ylabel("Position (Km)")
plt.show()