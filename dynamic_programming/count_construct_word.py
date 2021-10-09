def count_construct_word(target_word, word_bank, memo={}):

    if target_word in memo:
        return memo[target_word]

    if target_word == '':
        return 1

    ways_to_construct = 0
    for word in word_bank:
        if target_word.find(word) == 0:
            new_target_word = target_word[len(word):]
            ways_to_construct += count_construct_word(
                new_target_word, word_bank)

    memo[target_word] = ways_to_construct
    return ways_to_construct


print(count_construct_word('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print(count_construct_word('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print(count_construct_word('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print(count_construct_word('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4
print(count_construct_word('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
      ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # 0
