

my_table = [[45, 68, 33, 19, 57], 
            [90, 14, 29, 68, 22], 
            [82, 62, 55, 71, 20]]

print(my_table[1][1])

print(my_table[1])

sum = 0
for num in my_table[1]:
    sum += num

print("the sum of the second row is:", sum)


sum2 = 0
for i in range(len(my_table[2])): # the [2] ensures that you are counting the number of columns rather than the rows
 sum2 += my_table[2][i]

 print("The sum of the third row is:", sum2)

for row in range(len(my_table)):
    for col in range(len(my_table[row])):
        print(my_table[row][col], end=" ")