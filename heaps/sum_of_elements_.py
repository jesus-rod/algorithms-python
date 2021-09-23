# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).

from heapq import *

# 1. we put all numbers in a heap (n log n)
# we go through the heap and only add to our resul sum if index > k-1 and index < k2-1
# the -1 above because the k1 and k2 params are not 0th based
# then just return the sum


def find_sum_of_elements(nums, k1, k2):

    heapify(nums)
    endRange = len(nums)
    sum = 0
    for i in range(endRange):
        currentNum = heappop(nums)
        if i > k1-1 and i < k2-1:
            sum += currentNum

    return sum


def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
