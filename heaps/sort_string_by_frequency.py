from heapq import *


def sort_character_by_frequency(str):

    frequencyLetterMap = {}

    for letter in str:
        frequencyLetterMap[letter] = frequencyLetterMap.get(letter, 0) + 1

    maxHeap = []
    resultString = []
    for letter, frequency in frequencyLetterMap.items():
        heappush(maxHeap, (-frequency, letter))

    while maxHeap:
        topFrequency, topLetter = heappop(maxHeap)
        topFrequency = -topFrequency
        newStringPart = topFrequency * topLetter
        resultString.append(newStringPart)

    print(resultString)
    return "".join(resultString)


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
