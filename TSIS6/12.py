def is_palindrome(string):
    reversed_string = ''
    for char in reversed(string):
        reversed_string += char
    return string == reversed_string

string = input()
print(is_palindrome(string))
