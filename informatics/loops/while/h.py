n = int(input())
i, f0, f1 = 0, 0, 1
while i < n:
    next = f0 + f1
    f0 = f1
    f1 = next
    i += 1
print(f0)