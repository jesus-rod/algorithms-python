from math import floor


def mergeSort(nums):
    if len(nums) < 2:
        return nums

    length = len(nums)
    middle = floor(length / 2)
    left = nums[0:middle]
    right = nums[middle:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)
    return stitch(sortedLeft, sortedRight)


def stitch(left, right):
    results = []

    while len(left) and len(right):
        if left[0] <= right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    while len(left):
        results.append(left.pop(0))

    while len(right):
        results.append(right.pop(0))

    return results


algorithmToSort = mergeSort([10, 5, 3, 8, 2, 6, 5, 7, 9, 1])

print(algorithmToSort)
