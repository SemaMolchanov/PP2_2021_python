x = 1 #int
y = 2.8 #float
z = 3 + 4j #complex
f = 35e3 #float
g = -37.8e100 #float
print(type(x))
print(type(y))
print(type(z))
print(type(f))
print(type(g))

#we can convert one numeric type to another

#from int to float
a = float(x)

#fromt float to int
b = int(y)

#from int to complex
c = complex(x)

#it is impossible to convert from complex to any other numeric type

print((a))
print((b))
print((c))