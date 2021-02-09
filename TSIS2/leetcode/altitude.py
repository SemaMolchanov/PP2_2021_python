cur_alt = 0
highest_alt = cur_alt
gain = list(map(int, input().split()))
for i in range (len(gain)):
    cur_alt += gain[i]
    if cur_alt > highest_alt:
        highest_alt = cur_alt
print(highest_alt)
    

