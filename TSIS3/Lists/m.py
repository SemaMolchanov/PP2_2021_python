l1 = list(map(int, input().split()))
l2 = str()
for i in reversed(l1):
    l2 += str(i) + ' '
print(l2)