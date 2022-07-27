import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 6, 9, 10])


def findElement(array, element):
    for i in range(len(array)):
        if array[i] == element:
            print("The element index number is: ", i)


findElement(myArray, 6)
