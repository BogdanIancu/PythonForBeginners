import datetime


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


# Decorator
def logger(function):
    print(f"Function {function.__name__} called at {datetime.datetime.now()}")
    return function


@logger
def say_hello():
    print("Hello world!")


if __name__ == '__main__':
    main()
    say_hello()
