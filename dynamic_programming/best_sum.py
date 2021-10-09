def best_sum(target_sum, numbers, memo=None):

    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    best_combination = None

    for number in numbers:
        remainder = target_sum - number
        remainder_combination = best_sum(remainder, numbers, memo)

        if remainder_combination is not None:
            newCombination = remainder_combination + [number]
            if best_combination is None or len(newCombination) < len(
                best_combination
            ):
                best_combination = newCombination

    memo[target_sum] = best_combination
    return best_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
