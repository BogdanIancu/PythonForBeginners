import sys
from functools import reduce

maximum = 99


def hello_world():
    """
    This will just return \"Hello, world!\"
    :return: The \"Hello, world!\" message
    """
    global maximum
    maximum = 20
    if len(sys.argv) > 1:
        return f"Hello, {sys.argv[1]}!"
    else:
        return f"Hello, {maximum}!"


def addition(value1: int, value2: int = 1) -> int:
    """
    This function will add the two values
    :param value1: an integer
    :param value2: the other integer
    :return: the sum of the two
    """
    t = value1 + value2
    return t


def multiplication(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


def kwargs_example(**args):
    print(args)


def interchange(the_values):
    aux = the_values[0]
    the_values[0] = the_values[1]
    the_values[1] = aux


def reset_first_value_of_array(my_array):
    my_array = my_array[:]
    my_array[0] = 0


message = hello_world()
print(message)
print(maximum)
total = addition(4, 5)
print(total)

values = [8, 3]
interchange(values)
print(values)

just_an_array = [4, 5, 6]
reset_first_value_of_array(just_an_array)
print(just_an_array)

z = addition(value2=5, value1=9)
print(z)

y = addition(6)
print(y)

z = multiplication(4, 5, 6, 7, 8)
print(z)
z = multiplication(3, 7)
print(z)
kwargs_example(name="John", age=25, salary=4000)

another_function_that_does_addition = addition
print(another_function_that_does_addition(3, 2))

anonymous_function = lambda s, t: s * t
print(anonymous_function(6, 7))

result = reduce(lambda a, b: a-b, just_an_array)
print(result)

result = map(lambda a: a**2, just_an_array)
for value in result:
    print(value)

result = [value**2 for value in just_an_array if value >= 5]
print(result)

if __name__ == '__main__':
    hello_world()
