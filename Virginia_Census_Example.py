

file = open("Virginia_Census_2010.csv", "r", encoding="UTF-8-sig")

vmap = {}

for line in file:
    line = line.rstrip("\n")
    line = line.split(",")
    
    city = line[0].strip()
    population = int(line[1])

    vmap[city] = population

print("The dictionary contains", len(vmap), "entries.")
print(vmap)

print()
for city in vmap:
    print(city, "Has a population of", vmap[city])

print()
print("Blacksburg population:", vmap["Blacksburg"] )

vmap["Riner"] = 859
print()
print("Riner population:", vmap["Riner"])

bigger = ""
if vmap["Christiansburg"] > vmap["Blacksburg"]:
    bigger = "Christiansburg"
else:
    bigger = "Blacksburg"

difference = abs(vmap["Blacksburg"] - vmap["Christiansburg"])

print(bigger, "is larger by", difference, "people.")

smallest = ("Blacksburg", vmap["Blacksburg"])
for city, population in vmap.items():
    if population < smallest[1]:
        smallest = (city, population)

print()
print("The smallest city in Virginia is", smallest[0], "with a population of", smallest[1])