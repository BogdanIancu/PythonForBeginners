# single line comment

# multi
# line
# comment

"""this can be also
a multiline comment"""

# prints the result to the console
print(2 + 2)
print(1 < 2)
print(2 / 1)
print("Hello, world!")
print('Hello, people')

# constant values in Python
# are written in ALL CAPS
PI_VALUE = 3.14

# age is a variable
age = 35
print(age + 4)

# the type function
# returns the data type
# saved in a variable
print(type(age))

decimal_value = 8.4
print(decimal_value)
print(type(decimal_value))

complex_number = 4 + 5j
print(type(complex_number))

is_admin = False
print(type(is_admin))

# Python is dynamically-typed
# variables can store any data type
is_admin = 5
print(type(is_admin))

# Python is strongly-typed
# when it comes to conversions
# (does not use implicit conversions)
message = "age: " + str(age)
print(message)

# strings in Python are Unicode-based
name = "David 👶"
print(name)
name = "John"
print(name)

# strings are immutable
# changing them means creating a new value
surname = name
print(surname)
name = "something"
surname = "Something else"
print(name, surname)

# checks if the strings are equal
print(name == "something")
# repeats a string
print(name * 3)
# checks for the substring in the string
print("thing" in surname)

byte_literal = b'\x48\x65\x6c\x6c\x6f'
# will print b'Hello'
print(byte_literal)

hello = "Hello"
# string slicing
print(hello[1])
print(hello[1:4])
print(hello[1:])
print(hello[:2])

# string methods
another_string = hello.replace("H", "h")
print(another_string)
index = hello.find("l")
print(index)
index = hello.find("z")
print(index)

# formatting and escaping strings
vb1 = 'John'
vb2 = 3
text = ('Hello %s, you have %i messages' % (vb1, vb2))
print(text)
vb3 = f"{vb1} has \n{vb2} \"apples\"\\'oranges'"
print(vb3)


