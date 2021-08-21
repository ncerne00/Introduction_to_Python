'''
Project 2 - Scores Analysis and Bar Chart - Spring 2020
Author: <Nick Cerne, ncerne00>

This program <describe your program here>.

I have neither given or received unauthorized assistance on this assignment.
Signed:  <Nicholas Richard Cerne>
'''
import turtle


def draw_bar(integer):
    turtle.pensize(4)
    i = 0
    turtle.fillcolor("orange")
    while i <= 2:
        turtle.begin_fill()
        turtle.forward(integer * 20)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        i += 1
    turtle.end_fill

def position_turtle(integer):
        turtle.pensize(4)
        turtle.forward(integer * 20)
        turtle.right(180)

def turtle_write(string):
    turtle.forward(45)
    turtle.write(string)
        


compute_a_file = input("Compute a scores file? y / n ")

while compute_a_file == "y":
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
    turtle.left(90)
    draw_bar(count_90s)
    position_turtle(count_90s)
    draw_bar(count_80s)
    position_turtle(count_80s)
    draw_bar(count_70s)
    position_turtle(count_70s)
    draw_bar(count_60s)
    position_turtle(count_60s)
    draw_bar(below_60)
    position_turtle(below_60)

    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle_write("< 60")
    turtle_write("60s")
    turtle_write("70s")
    turtle_write("80s")
    turtle_write("90s")

    print(count_90s)
    print(count_80s)
    print(count_70s)
    print(count)

    compute_a_file = input("Compute another file? y / n")
else:
    print("Finished")