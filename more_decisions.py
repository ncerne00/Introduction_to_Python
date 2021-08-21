size = 344
weight = 170

if size < 120:
    if weight < 100:
        print("It fits")
    else:
        print("Too heavy")
else:
    print("Too big")

if size < 120 and weight < 100:
    print("It fits")
else:
    print("Too big or too heavy")


project_duration = 10

if project_duration > 30:
    project_duration += 14
else: 
    if project_duration > 14:
        project_duration += 7
    else: 
        if project_duration > 7:
            project_duration += 2

if project_duration > 30:
    project_duration += 14
elif project_duration > 14:
    project_duration += 7
elif project_duration > 7:
    project_duration += 2

print("project duration:", project_duration)

cars_sold = 15
if cars_sold ==  0:
    print("Unacceptable")
elif cars_sold < 10:
    print("Less than desired")
elif cars_sold < 20:
    print("Well done")
else:
    print("excellent")


if "alpaca" < "baboon":
   print("alpaca comes before baboon")
else:
    print("baboon comes before alpaca")

    if "&@%*" < "#$!^":
        print("&@%* comes first")
    else:
        print("#$!^ comes first") # strings are sorted via unicode, in this case # comes first, and letters are in alphabetical order

if ("alpaca" < "Baboon"):
    print("alpaca comes before Baboon")
else:
    print("Baboon comes before alpaca")   # capital letters come first before lowercase letters in the list of unicode 

event_description = "The ultimate party of the year!"

if "party" in event_description: # in, not in, these are membership operators
    print("I'm there")
if "studysession" not in event_description:
    print("I need to be intellectually challenged.")
print("all done")