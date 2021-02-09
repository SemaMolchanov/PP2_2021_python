nums = list(map(int, input().split()))
cnt = 0
for i in range (len(nums)):
    for j in range (1, len(nums)):
        if nums[i] == nums[j] and i < j:
            cnt += 1
print(cnt)