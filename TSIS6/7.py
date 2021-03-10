string = input()

lower_letters = [letter for letter in string if letter.islower()]
upper_letters = [letter for letter in string if letter.isupper()]

print(len(lower_letters), len(upper_letters))


