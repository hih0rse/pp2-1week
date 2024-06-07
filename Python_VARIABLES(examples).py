#Example:
x = 5
y = "John"
print(x)
print(y)
#Example:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#Example:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#Example:
x = "John"
# is the same as
x = 'John'
#Example:
a = 4
A = "Sally"
#A will not overwrite a
#Example:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#Example:
myVariableName = "John"
#Example:
MyVariableName = "John"
#Example:
my_variable_name = "John"
#Example:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Example:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Example:
x = "Python is awesome"
print(x)
#Example:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example:
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

#Example:
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

#Example:
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
