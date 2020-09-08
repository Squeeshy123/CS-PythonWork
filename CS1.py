import pygame;
def chaos():
    print("chaos") # output
    y = eval(input("How much should I print? ")) # Input
    x = eval(input("Number between 0 and 1: ")) # Input
    for i in range(y): # Loop
        x = 3.9 * x * (1-x) # assignment
        print(x) # output
# 3.9 * 0.15 * (1 - 0.15)

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
    print("Hey this is a program to convert the normal temprature to american temprature")
    c = int(input("What is the current temp? (C): "))
    f =  9 / 5  * c + 32
    print(str(c) + " is " + str(f) + " in Fahrenheit")

# Average score Calculator
def Scorese():
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
    Selector() # change this function to whatever 

if __name__=="__main__": # runs the main function
    main() 
