#
# Example from week of 1/27
#
# Experimenting with variable and assignment statements
#

"This is also considered a comment"

"""this is a perfectly valid string"""

distance = 420

count = 1

print("The distance is", distance)

distance = 750  #The distance is overwritten

print("The distance is", distance)

first_name = "Harry"

print("His first name is", first_name)

twice_as_far = distance * 2  # compute the extended distance

print("Twice as far is", twice_as_far)

count = count + 1

print("Count is now", count)

result = 13/4
print("13 / 4 is", result)

result = 13//4
print("13 / 4 is", result)

result = 13%4
print("13 % 4 is", result)

feet = 988 // 12
inches = 988 % 12
print("988 inches is", feet, "feet and", inches, "inches")

print("4 raised to the 5th power is", 4 ** 5)

import math 

print("Square root of 26:",  math.sqrt(26))