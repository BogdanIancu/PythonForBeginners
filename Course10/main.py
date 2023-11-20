import os
from pathlib import Path


def my_function():
    try:
        my_list = [6, 0, 3, 2]
        print(my_list[2])
        print(my_list[0] / my_list[3])
        raise KeyError
    except (IndexError, KeyError) as err:
        print(f"Check your index! Details: {err.args}")
    except:
        print("Something bad happened")
    finally:
        print("This will be always executed")


my_function()

text_file = open("file.txt", "w")
text_file.write("This is a message\n")
print(text_file.tell())
text_file.write("This is another message")
text_file.close()

with open("file.txt", "r") as another_text_file:
    another_text_file.seek(9)
    message = another_text_file.read()
    print(message)

print(another_text_file.closed)
print(another_text_file.mode)

os.rename("file.txt", "new_file.txt")
current_path = Path("new_file.txt")
print(current_path.exists())
print(current_path)
