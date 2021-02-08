from math import sqrt

def is_prime(x):
    if (x < 2):
        return False
    for i in range (2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True

n = int(input())
if n < 2:
    quit()
mindiv, i = 0, 2
while i <= n:
    if n % i == 0 and is_prime(i) == True:
        mindiv = i
        break
    i += 1
print(mindiv) 

