myList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# linear search
def searchInList(newList, value):
    for i in newList:
        if i == value:
            return newList.index(value)
    return "The value does not exist in the list."


print(searchInList(myList, 10))

# using IN operator
if 4 in myList:
    print(myList.index(4))
else:
    print("The value does not exist in the list")
