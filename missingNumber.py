# How to find the missing number in an integer of 1 to 10.

# equation of sum of series (1+2+3+.......+n = n(n+1)/2)

mylist = [1, 2, 3, 4, 5, 6, 8, 9, 10]


def findingNumber(list, n):
    sum1 = (10 * 11) / 2
    sum2 = sum(mylist)
    print(sum1 - sum2)


findingNumber(mylist, 10)
