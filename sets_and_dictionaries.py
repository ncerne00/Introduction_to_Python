

skills = {"Python", "Java", "Skateboarding", "Origami", "Woodworking"}

print(skills)

print("The number of skills in the set is", len(skills))

for skill in skills:
    print(skill)

print()
if "origami" in skills:
    print("Paper folding is my life.")

skills.add("Problem-Solving") #adds one element
skills.update(["SQL", "Graphic Design", "HTML", "Moonwalking"]) #adds several elements
print(skills)

skills.discard("Woodworking") # removes one element, doesn't pose an error if woodworking isnt in the list. The remove() command will.

needed_skills = {"Python", "Jui-Jitsu", "Origami"}

if skills <= needed_skills:
    print("This person has everything.")
else:
    print("This person does not have all of the needed skills.")

print("This person has these needed skills:", skills & needed_skills) # prints the elements that are in both sets

print("This person lacks these needed skills:", needed_skills - skills)

favorite_colors = {"Bob" : "Blue", 
                    "Sue" : "Purple",
                    "Dylan" : "Orange",
                    "Amy" : "Green",
                    "Max" : "Chartreuse"}

print(favorite_colors)
print("There are", len(favorite_colors), "favorite color entries.")

print("Dylan's favorite color is:", favorite_colors["Dylan"])

print("Amy's favorite color is:", favorite_colors.get("Amy"))

favorite_colors["Fred"] = "Firehouse Red" # gets added in as a new entry
favorite_colors["Max"] = "Brown"

print(favorite_colors)

favorite_colors.pop("Sue")

print(favorite_colors)

thing = {}

thing2 = set()

if "Sue" in favorite_colors:
    print("Sue's favorite color is", favorite_colors["Sue"])
else:
    print("I don't know what Sue's favorite color is.")

for person in favorite_colors:
    print(person)

for color in favorite_colors.values(): # .values prints the values, not the thing before the :
    print(color)

for person, color in favorite_colors.items():
    print(person + "'s favorite color is " + color)