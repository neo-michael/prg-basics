def f(palindrome):
    cleaned = ''.join(char.lower() for char in palindrome if char.isalnum())
    return cleaned == cleaned[::-1]
