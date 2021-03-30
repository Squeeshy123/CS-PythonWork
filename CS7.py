from math import *
from graphics import *
from time import sleep
import random
def time_and_a_half(): # PE 1
    hourly_rate = eval(input("What's your hourly rate? "))
    hours_worked = eval(input("How many hours did you work? "))
    if hours_worked >= 40:
        print("Pay estimate: " + str(hourly_rate * 1.5 * hours_worked))
    else:
        print("Pay estimate: " + str(hourly_rate * hours_worked))

def five_point_quizes(): # PE 2
    letter_grades = ["F","D","C","B","A"]
    input_grade = eval(input("What grade did they get? "))
    if input_grade > -1:
        print(letter_grades[int(input_grade)])
    else:
        print("F")

def hundred_point_quizzes():
    in_grade = eval(input("What is the students grade out of 100? "))
    if in_grade > 60:
        if in_grade > 69:
            if in_grade > 79:
                if in_grade > 89:
                    if in_grade >= 100:
                        print("A+")
                    else:
                        print("A")
                else:
                    print("B")
            else:
                print("C")
        else:
            print("D")
    else:
        print("F")

# PE 4 is pretty much the same as PE 3

def BMI_Calc(): # PE 5
    weight = eval(input("What's your weight (In pounds)? "))
    height = eval(input("What's your height (In inches)? "))
    bmi = (weight / height**2) * 720

    if bmi > 19 and bmi < 25:
        print("You have a healthy BMI of " + str(bmi))
    elif bmi > 25:
        print("Your BMI is " + str(bmi-25) + " over the heighest healthy amount (25)")
    elif bmi < 19:
        print("Your BMI is " + str(19 - bmi) + "under the lowest healthy amount (19)")
    else:
        print("your BMI is not within the healthy range")

def ticket_fine(): # PE 6
    mph = eval(input("how fast were they going? "))
    speed_limit = eval(input("what's the speed limit? "))
    mph_diff = mph - speed_limit
    price = 50
    if mph <= speed_limit:
        print("That's not speeding!")

    else:
        if mph > 90:
            price += 200
        else:
            price += mph_diff * 5
            print(price)

def baby_sitter_price(): # PE 7
    in_hours = eval(input("How many hours did the babysitter work? "))
    in_time = eval(input("When did the babysitter start their work? "))
    in_time_part = input("AM or PM? ").lower()

    left = in_hours + in_time
    time_after_nine = 0
    if in_time_part == "pm":
        print("OK")
        left += 12
        if left > 21:
            time_after_nine = left - 21
    print("Time they left " + str(left))
    print("Time Spent after nine " + str(time_after_nine))
    total = time_after_nine * 1.75 + (in_hours - time_after_nine) * 2.50
    print(total)

def senator_qualifications():  # PE 8
    age = eval(input("What is your age? "))
    years_in_us = eval(input("How many years have you been in the us? "))
    can_be_sen = False
    can_be_rep = False
    if age < 30:
        can_be_sen = False
    elif age >= 30 and years_in_us >= 9:
        can_be_sen = True
    
    if age < 25:
        can_be_rep = False
    elif age >= 25 and years_in_us >= 7:
        can_be_rep = True

    if can_be_sen:
        print("You can be a Senator")
    else:
        print("You cannot be a senator")
    
    if can_be_rep:
        print("You can be a House Representative")
    else:
        print("You cannot be a House Representative")

def easter_calc(): # PE 9 and 10
    year = eval(input("What year is it? "))
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d + 5)%7 
    result = (22 + d + e)
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        result -= 7
    month = "March"
    if result > 31:
        month = "April"
        result -= 30
    
    print(month + " " + str(result))

def is_leap_year(year = -1): # PE 11
    if year != -1:
        in_year = eval(input("Type in the year you think is a leap year? "))
        if in_year % 4 == 0 and in_year - floor(in_year/100) * 100 != 0:
            print(str(in_year) + " is a leap year!")
        else:
            print(str(in_year) + " is not a leap year")
    else:
        return in_year % 4 == 0 and in_year - floor(in_year/100) * 100 != 0

def month_day_year(): # PE 12
    months = [
        31,
        28,
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30, 
        31
    ]
    i_days = eval(input("what day is it? "))
    i_months = eval(input("what month is it? "))
    i_year = eval(input("What year is it? "))
    if i_months <= 12:
        if i_days < months[i_months]:
            print("date is valid")
        else:
            print("Date is not valid")
    else:
        print("Date is not valid")
    

def archery_target(): # PE 16
    window = GraphWin("Archery", 800, 800)
    size = 75
    center = Point(800/2, 800/2)
    text = Text(Point(100,25), "Points: ").draw(window)
    Circle(Point(800/2,800/2), size/4).draw(window)
    for i in range(0,4):
        c = Circle(Point(800/2,800/2), (size * 4) - (size * (i+1))).draw(window)
        c.setFill(color_rgb(255, 255 * (i % 2), 255 * i % 2))

    for i in range(0, 9):
        

        point = window.getMouse()
        Circle(point, 1).draw(window)
        current_points = 9
        dist_to_center = sqrt((point.x - center.x)**2 + (point.y - center.y)**2)
        
        if dist_to_center > 20:
            current_points -= 2
            if dist_to_center > 76:
                current_points -= 2
                if dist_to_center > 150:
                    current_points -= 2
                    if dist_to_center > 225:
                        current_points -= 2
                        if dist_to_center > 300:
                            current_points = 0
            
                                

        
        text.undraw()
        text = Text(Point(100,25), "Points: " + str(current_points)).draw(window)
        
def ball_bounce():
    window = GraphWin("Archery", 800, 800)
    running = True
    pos = Point(400,400)
    r = 10
    dir = Point(random.random(), random.random())
    speed = 10
    a = Circle(pos, r).draw(window)
    window.getMouse()
    a.setFill("black")
    for i in range(1,10000):
        sleep(0.01)
        a.move(dir.x * speed,dir.y * speed)
        if a.getCenter().x > 800 - r:
            dir.x *= -1
        if a.getCenter().x < 0 + r:
            dir.x *= -1
        if a.getCenter().y > 800 - r:
            dir.y *= -1
        if a.getCenter().y < 0 + r:
            dir.y *= -1
        if window.checkMouse():
            break
    
        
    
ball_bounce()