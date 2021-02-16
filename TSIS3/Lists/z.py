nums = input().split()
k = int(input())
step = k % len(nums)
for i in range (step, len(nums)):
    print(i, end=' ')
for i in range (step):
    print(i, end=' ')
