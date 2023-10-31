temperature = 30
humidity = 51

if temperature > 30:
    print("The watering system is starting...")
    if humidity > 50:
        print("Stopping the watering system "
              "because of raised humidity")
    else:
        pass
else:
    print("Idle mode")

name = "John"

if name == "Alice":
    print("It works!")

# temperature < 20 => start heating
# temperature >= 20 and temperature <= 25 => do nothing
# temperature > 25  => start AC
if temperature < 20:
    print("Started the heater")
elif 20 <= temperature <= 25:
    print("What an ideal weather")
else:
    print("Started AC")

# ternary operator, not if statement
message = "Heater" if temperature < 20 else "AC"
print(message)

flag = 0

match flag:
    case 0:
        print("System working")
    case 1:
        print("No power")
    case 2:
        print("No network connection")
    case 3:
        print("Server not responding")
    case _:
        print("Unknown error. Try to reset the sensor")

number = 1
while number < 10:
    if number % 2 == 1:
        print(number)
    number += 1

for char in "This is a string":
    print(char)

for i in range(5):
    print(f"{i} Something")

for _ in range(1, 4, 2):
    print(f"Something")

counter = 0
while counter < 9:
    if counter == 7:
        break
    counter += 1
    if counter == 5:
        continue
    print(counter)

print("Program finished")
