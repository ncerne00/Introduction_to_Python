
num = 1

while num <= 20: #while loops are good when you can't compute how many times it should loop
    print(num)
    num += 1

value = int(input("Enter a number between 20 and 30 inclusive: "))

while value < 20 or  value > 30: #locks into this loop until you get a valid value
    value = int(input("Invalid value. Please reenter: "))

full_str = ""
read_another = "y"

while read_another == "y":
    str = input("Enter a string: ")
    full_str += str
    read_another = input("Read another string (y or n)?")

print(full_str)

full_str = ""
str = input("Enter a string (or 'quit'):")

while str != "quit":
    full_str += str
    str = input("Enter a string (or 'quit'):")
    
print("Moving on")



