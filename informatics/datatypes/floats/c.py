a, b = map(float, input().split())
result = int(1)
total = float(a)
while total < b:
    a *= 1.7
    total += a
    result += 1
print(result)