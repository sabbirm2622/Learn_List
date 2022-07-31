myList = [1, 3, 5, 6, 7, 8, 9, 13, 42, 53, 12, 54, 60, 65, 2, 4, 14, 15, 16]


def isUnique(list):
    newList = []
    for i in list:
        if i in newList:
            print(i)
            return False
        else:
            newList.append(i)
    return True


print(isUnique(myList))
