s = input()
c = ''
if len(s) % 2 != 0:
    c += s[len(s)//2 + 1:]
    c += s[:len(s)//2 + 1]
else:
    c += s[len(s)//2:]
    c += s[:len(s)//2]
print(c)