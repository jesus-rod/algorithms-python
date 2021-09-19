# Input: Intervals [[2,3], [3,4], [5,6]]
# Output: [1, 2, -1]
# Explanation: The next interval of [2,3] is [3,4] having index ‘1’. Similarly, the next interval of [3,4] is [5,6] having index ‘2’. There is no next interval for [5,6] hence we have ‘-1’.

from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    n = len(intervals)
    result = [0 for x in range(n)]

    maxStartHeap, maxEndHeap = [], []

    for endIndex in range(n):
        heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
        heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))

    for _ in range(n):
        # retrieve interval with the highest end
        topEnd, endIndex = heappop(maxEndHeap)
        result[endIndex] = -1  # default result is -1
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex
            # put the interval back as it could be the next interval of other intervals
            heappush(maxStartHeap, (topStart, startIndex))

    return result


def main():

    result = find_next_interval(
        [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval(
        [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
