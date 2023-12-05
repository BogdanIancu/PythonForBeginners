import threading


def fibonacci_generator(maximum):
    a, b = 0, 1
    while a < maximum:
        yield a
        a, b = b, a + b
        print("Generator exit")


def fibonacci_function(maximum):
    numbers = []
    a, b = 0, 1
    while a < maximum:
        numbers.append(a)
        a, b = b, a + b
    print("Function exit")
    return numbers


def square_generator():
    while True:
        x = yield
        yield x ** 2


for item in fibonacci_generator(100):
    print(item)

for item in fibonacci_function(100):
    print(item)

generator = square_generator()
generator.__next__()
for i in range(6):
    value = generator.send(i)
    print(value)
    generator.__next__()


def my_function():
    for x in range(5):
        print(str(x) + "...")


t1 = threading.Thread(target=my_function)
t1.start()
print("Main thread")
t1.join()
print("Program ended")
