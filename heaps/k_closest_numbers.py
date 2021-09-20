from heapq import *


def find_closest_elements(arr, K, X):
    result = []
    maxHeap = []
    heappush(maxHeap, (0, X))  # push tuple of difference, number

    targetIndex = find_target(X, arr)

    for i in range(0, len(arr)):
        if i == targetIndex:
            continue
        currentDifference = abs(X - arr[i])
        if len(maxHeap) >= K:
            biggestDifferenceInHeap = -maxHeap[0][0]
            if currentDifference < biggestDifferenceInHeap:
                heappop(maxHeap)
                heappush(maxHeap, (-currentDifference, arr[i]))
        else:
            heappush(maxHeap, (-currentDifference, arr[i]))

    print(maxHeap)
    for _, num in maxHeap:
        result.append(num)
    return result


def find_target(target, array):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
