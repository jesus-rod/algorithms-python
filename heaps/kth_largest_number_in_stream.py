from heapq import *


class KthLargestNumberInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        for i in range(k):
            heappush(self.minHeap, nums[i])

        for i in range(k, len(nums)):
            self.add(nums[i])

    def add(self, num):
        if num > self.minHeap[0]:
            heapreplace(self.minHeap, num)
        return self.minHeap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
