#If x = 5, what is a correct syntax for printing the data type of the variable x?
x=5
print(type(x))
#using type(x) we can output the datatype of our x variable and output the "<class 'the class of x'>"
#in this certain example the datatype will be "int", because we input "x=5", where 5 is int

#The following code examples would print the data type of x, what data type would that be?

x="Hello World"
print(type(x))
#this will output string("str"), because we input text


x = 20.5
print(type(x))
#this will output "float", because our number has a decimal 

x = ["apple", "banana", "cherry"]
print(type(x))
#this will output "list", because we input array of ellements(list datatype)

x = ("apple", "banana", "cherry")
print(type(x))
#this will output "tuple", because we input several elements in single variable

x = {"name" : "John", "age" : 36}
print(type(x))
#this will output "dict", because we input separately the data in the way of key:value


x = True
print(type(x))
#this will output "bool", because we input boolean value(either "True" or "False")