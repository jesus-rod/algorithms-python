from heapq import *


def find_k_largest_numbers(nums, k):

    minHeap = []

    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        heapTop = -minHeap[0]
        if nums[i] > heapTop:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return minHeap


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
