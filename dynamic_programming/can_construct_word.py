def can_construct_word(target_word, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target_word in memo:
        return memo[target_word]
    if target_word == '':
        return True

    for word in word_bank:
        word_len = len(word)
        if target_word[0: word_len] == word:
            new_target_word = target_word[word_len: len(target_word)]
            if can_construct_word(new_target_word, word_bank):
                memo[target_word] = True
                return True

    memo[target_word] = False
    return False


print(can_construct_word('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # True
print(can_construct_word('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print(can_construct_word('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # True

print(can_construct_word('eeeeeeeeeeeeeeeeeeef',
      ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # False
