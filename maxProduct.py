import numpy as np

myArray = np.array([1, 3, 5, 6, 7, 8, 9, 12, 42, 53, 54, 60, 65, 2, 4, 14, 15, 16])

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i])+","+str(array[j])

    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)