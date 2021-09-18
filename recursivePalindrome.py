def isPalindrome(testVariable):
    print("string is", testVariable)
    endIndex = len(testVariable) - 1
    # Base case 1
    if len(testVariable) <= 1:
        print("len 1 means TRUE")
        return True

    elif testVariable[0] == testVariable[endIndex]:
        return isPalindrome(testVariable[1:endIndex])

    else:
        return False


isItPalindrome = isPalindrome("madam")
print(isItPalindrome)
