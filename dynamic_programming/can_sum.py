""""
Input: target: 7  numbers[3,4,5,7]
Output:  return True
Input: target: 7  numbers[2,4]
Output:  return False
"""


def can_sum(target, numbers, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        remainder = target - number
        can_sum_result = can_sum(remainder, numbers, memo)
        if can_sum_result:
            memo[target] = True
            return True

    memo[target] = False
    return False


print(can_sum(7, [3, 4, 5, 7]))  # true
print(can_sum(7, [2, 4]))  # false
print(can_sum(8, [2, 3, 5]))  # true
print(can_sum(300, [7, 14]))  # false
