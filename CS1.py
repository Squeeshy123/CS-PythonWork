#import pygame
# Chaotic function
def chaos():
    print("chaos") # output
    y = eval(input("How much should I print? ")) # Input
    x = eval(input("Number between 0 and 1: ")) # Input
    for i in range(y): # Loop
        x = 3.9 * x * (1-x) # assignment
        print(x) # output
# 3.9 * 0.15 * (1 - 0.15)


def invest(): # Investment calculator
    years_held = eval(input("How many years have you owned this: "))
    investment_amount = eval(input("Enter how many times you invested: "))
    principal = eval(input("Enter the initial investment value: "))
    apr = eval(input("Enter the annual gain: "))
    for i in range(years_held):
        principal = principal * (1 + apr)
    print("The value in", years_held, "years is: ", principal)
# Converts stones into pounds
def stoneConvert():
    print("This program converts stones into pounds")
    stones = eval(input("How many stones? "))
    pounds = stones * 14
    print(pounds)

# Converts kilometers into miles
def kilometerConvert():
    print("This program converts kilometers into miles")
    kilo = eval(input("How many kilometers? "))
    miles = kilo * 0.62
    print(kilo, "kilometers is", miles, "miles")

# make a sandwich function
def pbJ():
    print("make a sandwich")
    main_food = input("what is your main food item? ")
    second_food = input("what is your second food item? ")
    extras = input("any extras? ")
    print("ok, here's your sandwich: " + main_food + ", " + second_food + ", " + extras)
    done = input("Do you like your sandwich? y/n ")
    if(done == "y"):
        print("great!")
    if(done == "n"):
        print("well too bad we can't buy any more groceries and now we're out of " + second_food)

# makes a basic window using pygame (not part of the chapter)
def window():
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



# Celsuis to Fahrenheit calculator
def Faran():
    c = eval(input("How many tempratures do you want to convert?: "))
    for i in range(0, c):
        print("Hey this is a program to convert the normal temprature to american temprature")
        c = int(input("What is the current temp? (C): "))
        f =  9 / 5  * c + 32
        print(str(c) + " is " + str(f) + " in Fahrenheit")
    print("Done")

def Faran2():
    for i in range(0, 10):
        print("this program shows a data table of celsius conversion")
        f =  9 / 5  * i + 32
        print(str(c) + " is " + str(f) + " in Fahrenheit")
    print("Done")

# Average score Calculator
def Scorsese():
    scores = list()
    scores_amount = input("Enter how many elements you want:") # Ask how many scores there are
    print ("Enter numbers in array: ") # ask what the scores are
    for i in range(int(scores_amount)): # does the calculation for each score
        n = input("Score: ")
        scores.append(int(n))
    current_score = 0
    for i in range(int(scores_amount)):
        if(i != 0):
            current_score = scores[i] + scores[i - 1] / len(scores)
        else:
            print("not enough data, yet.....")
    print(current_score) # prints score once calculations are done
def test(): # just a test function, Ignore.
    print("start")
    for i in range(0): 
        print("hello")
    print("end")

def multiply():
    factor1 = eval(input("First factor: "))
    factor2 = eval(input("Second factor: "))
    print(factor1 * factor2)

def calculator():
    b = true
    while(b == true):
        case = 1
        function = input("What operator do you want to use? multiply, divide, add, subtract, stop")
        if(function == "multiply"): case = 1
        if(function == "divide"): case = 2
        if(function == "add"): case = 3
        if(function == "subtract"): case = 4
        if(function == "stop"): case = 5
        switch(case)
        {
            case 1: 
                
                break;
            case 2:
                dividend = eval(input("Whats the dividend: "))
                divisor = eval(input("Whats the divisor: "))
                print(dividend / divisor)
                break;
            case 3:
                add1 = eval(input("First number to add: "))
                add2 = eval(input("Second number to add: "))
                print(add1 + add2)
                break;
            case 4:
                sub1 = eval(input("Number to subtract from: "))
                sub2 = eval(input("Number to subtract by: "))
                print(sub1 - sub2)
                break;
            case 5: 
                b = false
                break;
        }


def brr(): # You can't multiply strings! Watch me.
    i = 0
    print("python go " + "b"+ "r" * 100)
def iteration(): # prints binary numbers up to 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376
    c = 1
    print(1)
    for i in range(500):
        c = c + c
        print(c)


def main():
    calculator() # change this function to whatever 

if __name__=="__main__": # runs the main function
    main() 
