list1 = [120, 23, 72, 34, 99]
print ("list= ", list1)

smallest_num = min(list1)
print("The smallest number in the list is", smallest_num)


alist = ["hello", "why", 89, 44, "cool"]
print(len(alist))

list_n = [1,1,1,1,1,2,2,2,2,4,2,2,2,2,]

print(freq(list_n,1))

def fastMode(dataset):
    n = 100
    lists = [0] * n
    
    for item in dataset:
        lists[item] += 2
        
    values = lists[0]
    for num in lists:
        if num > values:
            values = lists.