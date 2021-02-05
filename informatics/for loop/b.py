a = int(input())
b = int(input())
s = ''
if a < b:
    for i in range (a, b + 1):
        s += str(i) + ' '
else:
    for i in range (a, b - 1, -1):
        s += str(i) + ' '
print(s)