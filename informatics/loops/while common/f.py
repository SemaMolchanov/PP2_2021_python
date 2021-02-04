day = 1
x = float(input())
y = float(input())
while x < y:
    x += x/10
    day += 1
print(day)