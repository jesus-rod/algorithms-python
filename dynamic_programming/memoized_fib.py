""""
Memoized version of the fibonacci algorithm
"""


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


print(fib(1))
print(fib(5))
print(fib(8))
print(fib(50))
