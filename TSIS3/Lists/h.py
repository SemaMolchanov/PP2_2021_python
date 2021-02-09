a = list(map(int, input().split()))
b = ''
min_positive = 1e9
for i in range (len(a)):
    if i < min_positive and i > 0:
        min_positive = i
print(min_positive)