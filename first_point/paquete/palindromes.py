def is_palindrome(word: str) -> bool:
    try:
        flag = True
        if len(word) % 2 != 0:
            for char in range(len(word)):
                if char != (len(word)//2)+1:
                    if word[char] != word[-char-1]:
                        flag = False
                        break
        else:
            for char in range(len(word)):
                if word[char] != word[-char-1]:
                    flag = False
                    break
        return flag
    except TypeError:               #* Adding the exeption for TypeError 
        return "invalid Input"


print(is_palindrome(123))