from heapq import *


def find_k_frequent_numbers(nums, k):
    ocurrences = {}
    topNumbers = []

    # we create a hashmap with numbers and ocurrences
    for number in nums:
        if number in ocurrences:
            ocurrences[number] += 1
        else:
            ocurrences[number] = 1

    minHeap = []

    # we now add all the items to the heap but we limit it's size to K
    # because it a minheap, we will always pop the smallest element.
    # at the end, the heap will contain only the K biggest elements (by frequency)
    # because we kept popping the smaller ones when len(minHeap) > k
    for num, frequency in ocurrences.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)

    # finally we get the numbers from the frequency/nums tuple in the dictionary
    # and append that to our output array.
    while minHeap:
        _, topNum = heappop(minHeap)
        topNumbers.append(topNum)

    return topNumbers


def main():

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 8, 11, 3, 11], 2)))


main()
