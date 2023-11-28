import requests


def print_hi(name):
    print(f'Hi, {name}')
    response = requests.get("http://google.com")
    print(response.status_code)


if __name__ == '__main__':
    print_hi('PyCharm')

