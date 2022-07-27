# List operation

intergers = [1, 2, 3, 4, 5, 6]
stringList = ["sabbir", "morshed", "miazi"]
mixList = [1, 2, 3, "hello", "python"]
nestedList = [2, 3, 5, ["hello", "programmers"], [1, 3, 6, "Bangladesh", "China"]]


"""
# traversing
for i in nestedList:
    print(i)
"""

# Update List
intergers[2] = 34
print(intergers)

# insert into list
intergers.insert(4, 55)
print(intergers)

# append list
intergers.append(65)
print(intergers)

# Extend List
newInt = [12, 23, 45, 43]
intergers.extend(newInt)
print(intergers)

# Delete Element
# pop     # delete    # remove
print("Using pop method to delete")
mixList.pop()
print(mixList)
mixList.pop(1)
print(mixList)

# delete
print("Using del method to delete")
print(intergers)
del intergers[2]
print(intergers)
del intergers[3:5]  #slice method
print(intergers)

# remove
print("Using remove method to delete")
print(stringList)
stringList.remove("morshed")
print(stringList)


# Slice method
print("slice method")
myList = [2, 3, 5, 6, 7, 8]
print("Printing elements from 1 index to 4 index: ", myList[1:4])
myList[0:2] = [22, 33]
print("Updating list using slice: ", myList[:])

#List concatinate
print("\nList concatenating.....")
list1 = [1, 3, 4, 6]
list2 = [3, 5, 7, 9]
nList = list1 + list2
print(nList)

# maximum & minimum number in the list
print("Maximum number in the list: ", max(list1))
print("Minimum number in the list: ", min(list2))
