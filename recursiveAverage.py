def average(testVariable, currentIndex=0):
    if currentIndex == len(testVariable) - 1:
        return testVariable[currentIndex]

    if currentIndex == 0:
        return ((testVariable[currentIndex] + average(testVariable, currentIndex + 1)) / len(testVariable))

    return (testVariable[currentIndex] + average(testVariable, currentIndex + 1))


print(average([1, 2, 3, 4, 5, 6], 0))
