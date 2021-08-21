import os
print(os.getcwd())

input_file = open("one_foot.txt", "r")

for line in input_file:
    print(line, end="") 

print()

numbers_file = open("numbers.txt")

sum = 0
for line in numbers_file:
    print(line, end="")
    sum += int(line)
print()
print("The sum is:", sum)

