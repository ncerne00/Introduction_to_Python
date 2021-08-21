import random

my_list = random.sample(range(100, 1000), 10)
print(my_list)

sum = 0
for num in my_list:
    sum += num

average = sum / len(my_list)
print("The average is", average)

largest = 0
for num in my_list:
    if num > largest:
        largest = num

print("The largest value is:," largest)