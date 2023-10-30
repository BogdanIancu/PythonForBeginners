x = 5
y = 2

adding = x + y
print(adding)
subtraction = x - y
print(subtraction)
multiplication = x * y
print(multiplication)
division = x / y
print(division)
integer_division = x // y
print(integer_division)
remainder = x % y
print(remainder)
power = x ** y
print(power)
x = x + 2
print(x)
x += 2
print(x)
# the same with: x = x / 2
x /= 2
print(x)
z = ((2 + 3) * 6) ** 2
print("z =", z)

x = 5
print(x < y)
print(x <= 5)
print(x > y)
print(x >= y)
print(x == y)
print(x != y)

first_string = "abc"
second_string = "ayz"
copy = first_string[:]

print(first_string < second_string)
print(y := 3)
print(first_string == copy)

ok = True
print(not ok)

boolean_value = False
print(ok and (not boolean_value))
print(ok or boolean_value)
# shortcircuit
print(not ok and not boolean_value)
print(ok or not boolean_value)
print(first_string + second_string)

print(bool(first_string))
print(bool(""))

decimal_value = 4.35
integer_value = int(decimal_value)
print(integer_value)
