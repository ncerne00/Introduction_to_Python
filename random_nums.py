import random

print("Random float between 0 and 1:", random.random())

print("Random integer between 0 and 99:", random.randrange(100))
print("Random integer between 20 and 30:", random.randrange(20, 31))
print("Random integer between 50 and 100:", random.randrange(50, 101, 2))

print("random integer between 20 and 30:", random.randint(20,30)) #between 20 and 30 inclusive

colors = ["red", "green", "blue", "saddlebrown"]

for count in range(5):
    print(random.choice(colors))

if (random.choice([True, False])):
    print("go left")
else:
    print("go right")

flavors = ["vanilla", "chocolate", "strawberry", "mint chocolate chip", "rocky road"]

print("Sample size of 3:", random.sample(flavors, 3)) #prints a random sample, 3 is the sample size
print("Sample size of 4:", random.sample(flavors, 4))

my_sample = random.sample(range(10, 100), 20)
print("Twenty random two-digit numbers:", my_sample)

print(flavors)
random.shuffle(flavors)
print(flavors)