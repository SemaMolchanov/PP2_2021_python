left_border, right_border = map(int, input().split())
n = int(input())
if n in range(left_border, right_border):
    print('number ' + str(n) + ' is in the given range')
else:
    print('number ' + str(n) + ' is outside the given range')