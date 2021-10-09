"""
You are given a string that represents time in the format hh:mm.
Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible.
Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

Input: "?4:5?"
Output: "14:59"

Input: "23:5?"
Output: "23:59"

Input: "2?:22"
Output: "23:22"

Input: "0?:??"
Output: "09:59"

Input: "??:??"
Output: "23:59"
"""

# if s[0] == ?
# if s[1] == 4


def max_time(time):
    s = list(time)
    if s[0] == '?':
        canBeTwo = s[1] == '0' or s[1] == '1' or s[2] == '0' or s[1] == '3' or s[1] == '?'
        s[0] = '2' if canBeTwo else '1'
    if s[1] == '?':
        canBeThree = s[0] == '2'
        s[1] = '3' if canBeThree else '9'
    if s[3] == '?':
        s[3] = '5'
    if s[4] == '?':
        s[4] = '9'

    return "".join(s)


print(max_time('?4:59'))
print(max_time('23:5?'))
print(max_time('2?:22'))
print(max_time('0?:??'))
print(max_time('??:??'))
