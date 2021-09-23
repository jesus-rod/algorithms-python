
# Input: [7, 3, 5, 8, 5, 3, 3], and K=2
# Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have to skip 5 because it is not distinct and appeared twice.

# Another solution could be to remove one instance of '5' and '3' each to be left with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because it appeared twice.

# 1. Find frequency with a hashmap
# 2. into a minheap, push all elements as a tuple (frequency, number)
# 3. pop elements by least frequency, if frequency === 1 then add to results
# 4. check at the end if we still have something in our k. If we do, we just pop from the result

from heapq import *


def find_maximum_distinct_elements(nums, k):

    frequencyNumberMap = {}
    for num in nums:
        frequencyNumberMap[num] = frequencyNumberMap.get(num, 0) + 1

    minHeap = []
    for number, frequency in frequencyNumberMap.items():
        heappush(minHeap, (frequency, number))

    result = []

    while minHeap:
        smallestFrequency, leastFrequentNum = minHeap[0]

        if smallestFrequency == 1:
            result.append(leastFrequentNum)
            heappop(minHeap)
        elif k > 0:
            frequencyToUpdate, numToUpdate = heappop(minHeap)
            frequencyToUpdate -= 1
            heappush(minHeap, (frequencyToUpdate, numToUpdate))
            k -= 1
        else:
            break

    while k > 0:
        result.pop()
        k -= 1

    return len(result)


def main():

    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
