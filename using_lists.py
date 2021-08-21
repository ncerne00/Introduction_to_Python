import math

cities = ["Buffalo", "Austin", "Washington", "Seattle", "Dallas"]
print(cities[-1])

people_I_like = []

scores = [86, 100, 94, 82, 44]

mixed = ["ur mom", 18, 34]

print("There are", len(cities), "cities in the list.")

print("City at index 3:", cities[3])
print("City at index 0:", cities[0])

for city in cities:
    print(city)

cities = cities + ["Tilted Towers", "Denver"] #creating an entirely new string

for city in cities:
    print(city)

if "Tilted Towers" in cities:
    print("Tilted towers is in the list")
else:
    print("your mom gay")

cities.append("Jerusalem") #adding one element to the list, not creating a new one
print(cities)

cities.remove("Jerusalem")
print(cities)

cities[4] = "new york"
print(cities)

for city in cities: 
    city = city + "!"
    print(city)

print(cities)

num = 0
for city in cities:
    city = city + "!"
    cities[num] = city
    num+=1

print(cities)

