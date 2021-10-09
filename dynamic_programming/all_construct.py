"""
Given a target word, find all the possible ways to constructi t
Input: 'purple', ['purp', 'p', 'ur', 'le', 'purpl'])) 
Output: [
    [purp, le]
    [p, ur, p, le]
]

"""


def all_construct_word(target_word, word_bank, memo=None):

    if memo is None:
        memo = {}
    if target_word in memo:
        return memo[target_word]

    if target_word == '':
        return [[]]

    ways_to_construct = []
    for word in word_bank:
        if target_word.find(word) == 0:
            new_target_word = target_word[len(word):]
            new_way_to_construct = all_construct_word(
                new_target_word, word_bank, memo)

            for way in new_way_to_construct:
                way = [word] + way
                ways_to_construct.append(way)

    memo[target_word] = ways_to_construct
    return ways_to_construct


print(all_construct_word('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct_word(
    'abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct_word('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(all_construct_word('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(all_construct_word('eeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # 0
