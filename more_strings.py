

name = "Albert Einstein"

print(name.upper()) # creates an uppercase string 

print(name) # shows that name never changes

print(len(name))

name_in_lowercase = name.lower()
print(name_in_lowercase)

print(name.strip("Al"))

id = "truman4"

if id.isalpha():
    print("The id contains only alphabetic characters.")
elif id.isdigit():
    print("The id contains only digits.")
elif id.isalnum():
    print("The id contains only alphabetic letters and digits.")
else:
    print("YUH")

sentence = "She sells seashells by the seashore."

print("The number of 'sea' instances:", sentence.count("sea"))

print("The first occurence of 'sea' is at index:", sentence.find("sea"))

print(sentence.replace('sea', 'C')) # replaces all instances of sea with C

print(sentence)

print("sentence[10:15] =", sentence[10:15])

print("sentence[:6] =", sentence[:6])
print("sentence[:6] =", sentence[13:])

print("sentence[-6:] =", sentence[-6:])
print("sentence[-20:] =", sentence[-20:])

print(sentence[::2])

print(sentence[::-1])




