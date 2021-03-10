string = input()
words = string.split('-')
s = ''
for word in sorted(words):
    s += word + '-'

print(s[:-1])