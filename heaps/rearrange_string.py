from heapq import *

# 1. Create a frequency, letter hashmap
# 2. Push that into a maxheap
# 3. Take top two elements (they must be different)
# 4. If there is only one element in the heap, with more than a 1 as a frequency, we cant do it :(


def rearrange_string(str):
    frequencyLetterMap = {}

    for letter in str:
        frequencyLetterMap[letter] = frequencyLetterMap.get(letter, 0) + 1

    maxHeap = []
    for letter, frequency in frequencyLetterMap.items():
        heappush(maxHeap, (-frequency, letter))

    result = []
    while len(maxHeap) > 1:
        firstFreq, firstElem = heappop(maxHeap)
        secondFreq, secondElem = heappop(maxHeap)
        result.append(firstElem)
        result.append(secondElem)
        firstFreq = heappush_if_needed(maxHeap, firstFreq, firstElem)
        secondFreq = heappush_if_needed(maxHeap, secondFreq, secondElem)

    # checking if there is something still in the heap.
    # if there is, we need to add it to our result
    while maxHeap:
        firstFreq, firstElem = heappop(maxHeap)
        heappush_if_needed(maxHeap, firstFreq, firstElem)
        result.append(firstElem)

    return "".join(result)


# Clean up code, avoid duplication
def heappush_if_needed(maxHeap, frequency, letter):
    frequency = -frequency
    if frequency > 1:
        frequency -= 1
        heappush(maxHeap, (-frequency, letter))
    return frequency


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
