#here x i sa global variable
#it can be used both inside and outside the function
x = "awesome"

def my_function():
    print("python is " + x)

my_function()

#now we'll create local variable y
y = "awesome"
def my_func():
    y = "fantastic"
    print("python is " + y)

my_func()
print("Python is " + y)

#now we'll create global variable inside the function

def func():
    global z
    z = "fantasic"
    print("Python is " + z)

func()
print("Python is " + z)

#we can refer to the global var
#inside the function to change its value

a = "fantastic"
def last_func():
    global a
    a = "amazing"
    print("Python is " + a)

last_func()
