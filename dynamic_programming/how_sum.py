""""
Input: target: 7  numbers[3,4,5,7]
Output:  return [3,4] or [7]
Input: target: 7  numbers[2,4]
Output:  return None
"""

# Base case 1: If target is zero, return []
# Base case 2: If target is less than zero, return None
# 1. We recursively call how_sum substituting the target with target-num[i]
# 2. We check if the result is not None
# 3. We append the current number to our result
# 4. To memoize create a memo dict
# 5. Check at the beginning if our target is already in the memo dict, return its value if so
# 6. Put everywhere where there is a return a new memo allocation -> memo[target] = returnVal


def how_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for number in numbers:
        remainder = target - number
        remainderResult = how_sum(remainder, numbers, memo)
        if remainderResult is not None:
            remainderResult.append(number)
            memo[target] = remainderResult
            return remainderResult

    memo[target] = None
    return None


print(how_sum(7, [5, 3, 4, 7]))  # [4,3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None
