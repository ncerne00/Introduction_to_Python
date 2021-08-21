
num1 = 500
num2 = 100
name = "Albert Einstein"
price = 50

if num1 > 200:
    print("Virginia")

if price < 38.20:
    print("California") 
    print("Maine")

if num1 == 222: #'==' are they equal?, = sets them equal
    price = price*2
    print("Texas")

if num2 != 333:
    print("Florida")

if num1 - num2 >= 400:
    print("Ohio")

    if 450 <= num1 <= 550:
        print("In range")

if num1 == 999:
    print("Colorado")
else:
    print("Nevada")
    
if len(name) > 12:
    print("That is a long name.")
else: 
    print("Montana")

thirsty = True
found = False

flag = (num1 + 7) * num2 >= 5000 # stores as a boolean; true or false
print("flag is", flag)

if num2 < num1 and len(name) == 15:
    print("Alaska")

if not thirsty or name == "Albert Einstein":
    print("Utah")



print("All done.") #not governed by the if statements