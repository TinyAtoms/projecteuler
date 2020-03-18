


def is_palindrome(word):
    l = len(word)
    if l % 2:
        left = word[:int(l/2)]
        right =word[int(l/2)+1:][::-1]
    else:
        left = word[:int(l/2)]
        right =word[int(l/2):][::-1]
    return (left == right)