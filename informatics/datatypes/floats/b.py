a, b = map(float, input().split())
day = 1
while a < b:
    a *= 1.7
    day += 1
print(day)