
def chaos():
    print("chaos")
    y = eval(input("How much should I print? "))
    x = eval(input("Number between 0 and 1: "))
    for i in range(y):
        x = 3.9 * x * (1-x)
        print(x)
# 3.9 * 0.15 * (1 - 0.15)

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


def Faran():
    c = int(input("What is the current temp? (C): "))
    f =  9 / 5  * c + 32
    print(str(c) + " is " + str(f) + " in Fahrenheit")


def Scorese():
    scores = list()
    scores_amount = input("Enter how many elements you want:")
    print ("Enter numbers in array: ")
    for i in range(int(scores_amount)):
        n = input("Score: ")
        scores.append(int(n))
    current_score = 0;
    for i in range(int(scores_amount)):
        if(i != 0):
            current_score = scores[i] + scores[i - 1] / len(scores)
        else:
            print("not enough data, yet.....")
    print(current_score)

def brr():
    i = 0
    print("python go " + "b"+ "r" * 100)
def iteration():
    c = 1
    for i in range(500):
        
        c = c + c
        print(c)

def main():
    iteration()

if __name__=="__main__": 
    main() 
"""
    True or False
        False
        True
        True
        False
        False
        True
        False
        True
        False
        False

    Multiple Choice
        B
        D
        C
        B
        B
        D
        B
        B
        C
        D

    Compare and contrast
    
    What the computer is made of vs what is on the computer
        A set of calculations to execute vs a collection of functions performing together
    The language that computers use and the language that humans use
        An interpreter does one statement and the compiler scans the whole program


The 5 parts
    The way the computer wants it and the way that humans can understand it
        Input devices are such as keyboard and mouse that will tell the cpu that something happened
        The cpu is the brains of the operation and can crunch number and equations, as long as it’s told what to do
        Main memory saves all the long term data, like files programs and cat pictures.
        Secondary memory is short term data storage and will save stuff like where your mouse is on the screen or what netflix show your watching
        Output devices are mainly the monitor and will display what the cpu tells it.



        
"""