#function to find smallest values
list1 = [10, 20, 1, 45, 99]

print("smallest element is:", min(list1))

#function takes string, returns new string where words are capitalized
name = "math"
print(name.upper())

#list of numbers with each item squared
def printValues():
    l = list()
    for i in range(1,15):
        l.append(i**2) #append adds another number behind
    print(l)

printValues()



#take two number
first = [1,2,3,4,5]
second = [6,7,8,9,10]
    
third = [x + y for x, y in zip(first, second)]
print("third" , third) 


#chapter10
#10
def word_count(list, length):
    count=0
    for word in list:
        count=count+1
    return count
word_count(mylist,4)

#11
def sumEven(lst):
    sum_ = 0
    for i in lst:
        if i % 2 != 0:
            sum_+= i
        else:
            return sum_
lst = []

for i in range(100):
    lst.append(random.randint(0,1000))

print(lst)

#12

def count_numer_sam(samnumber):
    return_count = 0
    for element in samnumber:
        if element == "sam":
            break
        return_count = return_count+1       
if __name__ == '__main__':
    lst = lst = ["hi", "code", "word", "sam", "bye"]
    name = 'sam'
    if name not in lst:
        print(f'<{name}> not in list')
    else:
        result = count_to_name(lst, name)
        print(f'<{name}> appear at number <{result}> in list')

