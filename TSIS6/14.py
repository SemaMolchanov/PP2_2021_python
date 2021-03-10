def is_pangram(string):
    letters = [char for char in string.lower() if ord(char) in range(97, 123)]
    return len(set(letters)) == 26

string = input()
print(is_pangram(string))