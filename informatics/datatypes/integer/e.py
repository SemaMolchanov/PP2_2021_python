k, n = map(int, input().split())
print(str((n - 1)//k + 1) + ' ' + str((n - 1) % k + 1))