import gc
from array import array
from collections import deque

empty_list = []

list1 = [1, 2, 7, 9, 9]
print(len(list1))
print(list1.count(9))
list1.append(5)
print(list1)
list1.pop()
print(list1)
list1.insert(4, 3)
print(list1)
print(list1.index(9))
list1.remove(3)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
print(list1[3])

print(list1 == [1, 2, 7, 9, 9])
print(7 in list1)
print(9 not in list1)

list2 = [5, 1, 7]
list3 = list1 + list2
print(list3)
list4 = [0] * 10
print(list4)

list5 = list2[:]
list5[0] = 100
print(list2[0])

list6 = list2[-2:]
print(list6)
list7 = list1[::2]
print(list7)
# list7.pop(1)
# print(list7)

first_value, second_value, third_value = list7
print(first_value)

first_value, *others = list7
print(first_value)
print(others)
*others, last_value = list7
print(others)
print(last_value)
del list7[0:2]
print(list7)

s = 0
for value in list3:
    s += value
print(s)

i = 0
while i < len(list3):
    print(list3[i])
    i += 1

my_list = [["John", 2000], ["Maria", 3000], ["George", 2500]]
salaries = [item[1] for item in my_list]
print(salaries)

my_array = array("i", [1, 2, 3, 4])
print(my_array)
print(my_array[2])

books_stack = []
books_stack.append("The Davinci Code")
books_stack.append("Homo Deus")
books_stack.append("Sapiens")

print(books_stack.pop())
print(books_stack.pop())

print()
persons_queue = []
persons_queue.append("Maria")
persons_queue.append("John")
persons_queue.append("George")

print(persons_queue.pop(0))
print(persons_queue.pop(0))

print()
another_queue = deque()
another_queue.append("Maria")
another_queue.append("John")
another_queue.append("George")

print(another_queue.popleft())
print(another_queue.popleft())

matrix = [[1, 0, 1], [2, 1, 2], [3, 2, 1]]
print(matrix)

for line in matrix:
    line_to_be_printed = ""
    for value in line:
        line_to_be_printed += str(value) + " "
    print(line_to_be_printed)

my_tuple = (1, 8, 3, 2)
print(my_tuple.count(8))
print(my_tuple.index(3))
print(my_tuple[1])

PI = (3.14,)
# ...
print(PI[0])
# PI[0] = 2.45 # will not work

x = 5
y = 3

(x, y) = (y, x)
print(x, y)

# dictionary
phone_book = {"Albert": 734123566, "Bob": 767236556, "David": 746784531}
print(phone_book["David"])
phone_book["Maria"] = 721678445
print(phone_book)

if "Karla" in phone_book:
    print(phone_book["Karla"])

print(phone_book.get("Karla", "Not found"))

my_set = {2, 3, 1, 5, 6, 1}
print(my_set)
if 1 in my_set:
    print("It's there")
else:
    print("Is not there")

my_new_list = list(my_set)
print(my_new_list)

set2 = set(list3)
print(set2)

print(my_set & set2)

my_dictionary = {x: x**2 for x in range(5)}
print(my_dictionary)

another_dictionary = {}
for item in range(5):
    another_dictionary[item] = item ** 2

print(another_dictionary)

gc.collect()
