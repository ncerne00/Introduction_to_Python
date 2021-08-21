
school =  "Virginia Tech"
for ch in school: # for loops work through a particular sequence of values, including strings
    print(ch)

count = 0
for ch in school:
    if ch == "i":
        count += 1
print("There are", count, "i's in", school)

partial = ''
for ch in school:
    partial += ch
    print(partial)

for num in range(10):
    print(num)

print()
for num in range (20, 30):
    print(num)

print()
for num in range(1, 15, 2): #third value is a step value, goes through range 1 - 15 in increments of 2
    print(num)

print()
for num in range(5, 101, 5):
    print(num)

print()
for num in range(10, 0, -1): #negative step value lets us count backwards, stops at 1 not 0 
    print(num)

sum = 0
for num in range (1, 71):
    sum += num
print("The sum of the integers from 1 to 70, inclusive is:", sum)

for num in range(1, 11):
    print("2 to the power", num, "is", 2 ** num)

for row in range(20):
    for col in range(20):
        print("#", end="")
    print()

    
   
