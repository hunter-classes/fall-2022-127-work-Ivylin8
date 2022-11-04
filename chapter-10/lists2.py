##question 4 

def average (numlist):
    total = 0
    for num in numlist:
        total = total + num
        
    return total / len(numlist)



###question 6

import random

xs = []


for i in range(3):
    xs.append(random.randint(0,50))

def sum_of_squares(xs):

    squared = i ** i

    sum_of_squares = squared + squared + squared

    return sum_of_squares

print (sum_of_squares(xs))
