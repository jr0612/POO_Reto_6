def find_anagrams(words: list) -> list:
    """
    a function that finds anagrams from a list of words
    param: words: list
    return: anagrams: list
    """
    # ! raise error
    if not isinstance(words, list):
        # raise error for not list input
        raise TypeError("the input is not a list")
    if not words:
        # raise error for empty list
        raise ValueError("the input list is empty")
    if not all(word.isalpha() for word in words):
        # raise error for non-alphabetic characters
        raise ValueError("the input list contains non-alphabetic characters")

    anagrams_dict = {}
    for word in words:
        sort_word = "".join(sorted(word))
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]
    anagrams = [
        word for group in anagrams_dict.values() if len(group) > 1 for word in group
    ]
    return anagrams


def perform_find_anagrams(words):
    try:
        return find_anagrams(words)
    except Exception as identifier:
        print("error: ", identifier)


print(perform_find_anagrams(["hello", "world", "hello"]))
print(perform_find_anagrams(["dog", "god", "cat"]))
print(perform_find_anagrams(["ab", "123"]))
print(perform_find_anagrams([]))
print(perform_find_anagrams(134))
