'''Consider the following code:
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
What will be the printed result?'''
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#Python is awesome, because we declared x="awesome" in the separate line

#Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x = "fantastic"

'''Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
What will be the printed result?
'''
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#Python is fantastic, because using the "global" we made that so x will be "fantastic", no matter what was written before?
