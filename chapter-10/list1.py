list = [76, 93.3, 'hello', True, 4, 76]

list.append("apple")
list.append(76)
list.insert(3, "cat")
list.insert(0, 99)

print(list.index("hello"))
print(list.count(76))
list.remove(76)
list.pop(list.index(True))

print(list)