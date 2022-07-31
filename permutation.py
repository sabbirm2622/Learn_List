# Permutation of two lists


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

lst1 = [1, 2, 4, 5, 6, 12]
lst2 = [1, 4, 2, 6, 12, 5]
print(permutation(lst1, lst2))