arr = list(map(int, input().split()))
min_positive = min(i for i in arr if i > 0)
print(min_positive)