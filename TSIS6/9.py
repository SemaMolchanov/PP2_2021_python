from math import sqrt

def is_prime(n):
    if (n < 2):
        return False
    for i in range(2, int(sqrt(n))):
        if (n % i == 0):
            return False
    return True

n = int(input())
print(is_prime(n))