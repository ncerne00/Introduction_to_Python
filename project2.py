'''
Project 2 - Scores Analysis and Bar Chart - Spring 2020
Author: <Nick Cerne, ncerne00>

This program <This program reads in a list of integers from any file name and returns the maximum, the minimum, the average, and the number of integers
in the list. It also draws a clustered bar chart with random colors based on the percentage of each number range.>.

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Nicholas Richard Cerne>
'''
import turtle, random

#draw bar draws each column and also writes which number range it is, also picks a random color for each bar
def draw_bar(length, numrange):
    colors = ["red", "blue", "brown", "yellow", "orange", "green", "purple", "maroon"]
    turtle.fillcolor(random.choice(colors))
    turtle.begin_fill()
    turtle.left(90)
    for i in range(2):
        turtle.forward(length * 20)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(7)
    turtle.right(90)
    turtle.forward(5)
    turtle.write(numrange)
    turtle.right(180)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(7)
    turtle.left(90)
    turtle.pendown()

    
#this function positions the turtle to get ready for the next draw_bar function
def position_turtle():
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    

#Start of program
compute_a_file = input("Compute a scores file? y / n ")
#while compute_a_file = yes keep this loop running, AKA keep prompting user for a new file name. Then run through the loop and compute.
while compute_a_file == "y":
    turtle.reset()
    which_file = input("What is the name of your file? ")
    score = open(which_file, "r")
    highest_score = 0
    a_list = []
    count_90s = 0
    count_80s = 0
    count_70s = 0
    count_60s = 0
    below_60 = 0

    sc = score.readlines()[1:]
    num_scores_1 = len(sc[1:])
    score.seek(0)
    assignment = score.readline()
   


    count = 0
    max = 0
    min = 100
    sum = 0
    #for loop that checks if the next number is greater than max, and then sets it to it. Same goes for min. Also checks what number range the number is in
    for line in sc:
        num = int(line.split('\n')[0])
        count += 1
        if (max < num):
            max = num
        if (min > num):
            min = num
        if (num >= 90 ):
            count_90s += 1
        elif (num >= 80 and num < 90):
            count_80s += 1
        elif (num >= 70 and num < 80):
            count_70s += 1
        elif (num >= 60 and num < 70):
                count_60s += 1
        else:
            below_60 += 1
        sum += num

    average = sum / num_scores_1
    print("Your results for", assignment, end="")
    print("Your maximum is", max)
    print("Your minimum is", min)
    print("Your average is", round(average, 2))
    print("The number of scores in", num_scores_1)
    
    turtle.penup()
    turtle.goto(-125, -250)
    turtle.pendown()
    draw_bar((count_90s / count) * 20, "90s")
    position_turtle()
    draw_bar((count_80s / count) * 20, "80s")
    position_turtle()
    draw_bar((count_70s / count) * 20, "70s")
    position_turtle()
    draw_bar((count_60s / count) * 20, "60s")
    position_turtle()
    draw_bar((below_60 / count) * 20, "< 60s")
    
    turtle.penup()
    turtle.forward(5)
    turtle.left(180)
   
    turtle.hideturtle()

    compute_a_file = input("Compute another file? y / n")
else:
    print("Finished")
