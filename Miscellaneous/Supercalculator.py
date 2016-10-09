import itertools
import math
def distance(x1, y1, x2, y2):
    x = ((x2-x1)**2)
    y = ((y2-y1)**2)
    answer = math.sqrt(x+y)
    input("-----------------------------------------------------\nThe distance of the line is " + str(answer) + "\n-----------------------------------------------------\nPress enter to exit")
    quit()
def midpoint(x1, y1, x2, y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    input("-----------------------------------------------------\nThe midpoint of your line is " + str(x) + "," + str(y) + "\n-----------------------------------------------------\nPress enter to exit")
    quit()
def slope(x1, y1, x2, y2):
    x = x1-x2
    y = y1-y2
    answer = x/y
    input("-----------------------------------------------------\nThe slope of your line is " + str(answer) + "\n-----------------------------------------------------\nPress enter to exit")
    quit()
def scientificnotation(x): 
    if x > 10:
        for i in itertools.count():
            x /= 10
            if x < 10:
                input("-----------------------------------------------------\n" + str(x) + " x 10^" + str(i+1) + "\n-----------------------------------------------------\nPress enter to exit")
                quit()
                break
    else:
        for i in itertools.count():
            x *= 10
            if x > 0.9:
                input("-----------------------------------------------------\n" + str(x) + " x 10^" + str((i*-1)-1) + "\n-----------------------------------------------------\nPress enter to exit")  
                quit()
                break               
response = int(input("Press the corresponding number\n 1.scientific notation conversion\n 2.midpoint\n 3.slope\n 4.distance\n"))
if response == 1:
    x = float(input("Enter the number you would like to put in scientific notation"))
    scientificnotation(x)
if response == 2:
    x1 = float(input("Enter your x1 value"))
    y1 = float(input("Enter your y1 value"))
    x2 = float(input("Enter your x2 value"))
    y2 = float(input("Enter your y2 value"))
    midpoint(x1,y1,x2,y2)
if response == 3:
    x1 = float(input("Enter your x1 value"))
    y1 = float(input("Enter your y1 value"))
    x2 = float(input("Enter your x2 value"))
    y2 = float(input("Enter your y2 value"))
    slope(x1,y1,x2,y2)
if response == 4:
    x1 = float(input("Enter your x1 value"))
    y1 = float(input("Enter your y1 value"))
    x2 = float(input("Enter your x2 value"))
    y2 = float(input("Enter your y2 value"))
    distance(x1,y1,x2,y2)
