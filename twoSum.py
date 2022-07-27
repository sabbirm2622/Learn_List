mylist = [1, 2, 3, 4, 6, 7, 9]


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print("index", i, "and index", j, "=", target)


twoSum(mylist, 7)
