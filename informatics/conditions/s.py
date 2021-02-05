a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a*a + b*b == c*c:
        print('rectangular')
    elif a*a + b*b > c*c:
        print('acute')
    elif a*a + b*b < c*c:
        print('obtuse')
else:
    print('impossible')