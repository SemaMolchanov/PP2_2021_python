from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range (2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True

n = int(input())
if (is_prime(n) == True):
    print("YES")
else:
    print("NO")