a = float(input())
b = float(input())
c = float(input())
if abs(c - (a + b)) <= 0.00000001:
    print('YES')
else:
    print('NO')