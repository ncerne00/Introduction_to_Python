

dogs = ["German Shepherd", "Beagle", "Boxer", "Poodle", "Great Dane", "Golden Retriever", "Labradoodle"]

print(dogs)

slice = dogs[2:6]
print(slice)

print(dogs[1:7])

print(dogs[4:])

print(dogs[:-3])

print(dogs[::2])

print(dogs[::-1])

print(dogs[len(dogs):0:-1]) #prints it backwards


# --------------------------------- 

dogs.append("Husky") #takes one element

print(dogs)

dogs.extend(["Chihuahua", "Rottweiler"]) #extend takes a list of elements

print(dogs)

dogs.insert(3,"Doberman")

print(dogs)

dogs[7] = "Black Lab"

print(dogs)

dogs.remove("Poodle")

dogs.pop()
print(dogs)

dogs.pop(1)
print(dogs)

index_of_blacklab = dogs.index("Black Lab")
print("Black Lab is at index", index_of_blacklab)

print("Count of 'Boxer':", dogs.count("Boxer"))

dogs.reverse()
print(dogs)

dogs.sort()
print(dogs)
p 