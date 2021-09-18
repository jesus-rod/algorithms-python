def balanced(testVariable, startIndex=0, currentIndex=0):

    closedP = ")"
    openP = "("

    # Validation case
    if testVariable[0] == "closedP":
        return False

    # Base case: if at end. It must be a closing parentheses
    if currentIndex == len(testVariable) - 1:
        if testVariable[currentIndex] == openP:
            return False
        if

    # if it is an open parentheses, keep it as the start index
    elif testVariable[currentIndex] == openP:
        return balanced(testVariable, startIndex=currentIndex, currentIndex=currentIndex+1)
    elif testVariable[currentIndex] == closedP:
        if testVariable[currentIndex - 1] == openP:
            return balanced(testVariable, startIndex=startIndex+1, currentIndex=currentIndex+1)
        else:
            return False

    return None
