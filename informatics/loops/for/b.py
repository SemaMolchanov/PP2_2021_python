a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = ''
for i in range (a, b + 1):
    if i % d == c:
        x += str(i) + ' '
print(x)
        