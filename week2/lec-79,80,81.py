#palindrome function

def is_palindrome(word):
    reversed_word = word[::-1]
    if word ==reversed_word:
        return reversed_word == word[::-1]
    return False