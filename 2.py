import sys
print(sys.version)

if 5 > 2:
    print("Five is greater than two!")

#print("Hello, World!")
print("Cheers, Mate!") #this is comment

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"
myfunc()

print("Python is " + x)