

def compute_area(length, width): #length and width are parameters
    return length * width

def print_instructions(): # it is convention to keep your functions at the top of python programs
    print("Use these controls to play the game:")
    print("Up arrow - move forward")
    print("Down arrow - move backward")
    print("And so on...")

def say_hi(name):
    print("Hi,", name)  

def say_hello(name, greeting): 
    print('Hello', name + ",", greeting)

def is_even(num):
    if num % 2 == 0:
        return True 
    else:
        return False

def is_odd(num): #much cleaner approach
    return num % 2 != 0

def compute_total(unit_price, quantity, tax_rate):
    subtotal =  unit_price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

def get_total(unit_price, quantity, tax_rate = 0.06):
    subtotal =  unit_price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total
#Returns the sum of the two arguments
def compute_sum(num1, num2):
    return num1 + num2

def add(num1, num2):
    """Returns the sum  of num1 and num2"""
    return num1 + num2



area = compute_area(12, 4) #12 and 4 are arguments
print("The area is:", area)

#or

print("The area is:", compute_area(10, 5))

print_instructions()

say_hi("Jimmy")
say_hi("Bob")

say_hello("Garret", "How are you") #the order matters when it comes to writing your arguments/parameters
say_hello("Harry", "yer a wizard")
say_hello(greeting = "How's it going", name = "Jim")

if is_even(25):
    print("25 is even")
else:
    print("25 is odd")

print(is_odd(3))

print("Your total is:", compute_total(5.29, 4, .06))
print("Your total is:", compute_total(34.98, 2, .065))
print("The total is:", get_total(9.99, 4))