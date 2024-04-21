def find_anagrams(words: list) -> list:
    anagrams_dict = {}
    for word in words:
        sort_word = "".join(sorted(word))
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]
    anagrams = [word for group in anagrams_dict.values() if len(group) > 1 for word in group]
    return anagrams