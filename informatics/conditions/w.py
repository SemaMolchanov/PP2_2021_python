a = int(input())
b = int(input())
c = int(input())
sides = [a, b, c]
sides.sort()
if sides[0] + sides[1] <= sides[2]:
    print("impossible")
    quit()
sides[0] = sides[0]**2 + sides[1]**2
sides[2] = sides[2]**2
if sides[0] == sides[1]:
    print("right")
else:
    if sides[0] > sides[2]:
        print("acute")
    else:
        print("obtuse")