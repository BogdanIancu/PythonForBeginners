import datetime
import functools


class MyIterableType:
    def __init__(self):
        self.value = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < 10:
            self.value += 2
            return self.value
        else:
            raise StopIteration


def main():
    my_list = [3, 5, 1]
    my_string = "aha"

    # my_list is iterable
    # i is an iterator
    for i in my_list:
        print(i)

    # the same is my_string
    for c in my_string:
        print(c)

    # this is a custom iterator
    my_iterator = MyIterableType()
    for i in my_iterator:
        print(i)


# Decorator
def logger(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Function {function.__name__} called at {datetime.datetime.now()}")
        return function(*args, **kwargs)
    return wrapper


@logger
def say_hello():
    print("Hello world!")


@logger
def addition(x, y):
    return x + y


if __name__ == '__main__':
    main()
    say_hello()
    print(addition(3, 7))
    print(say_hello.__name__)
