import csv
import numpy

with open('general_rates.csv')as csvfile:
    for i in csv.reader(csvfile):
        print(','.join(i))
    print('')
    