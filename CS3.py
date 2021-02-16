#import numpy as np
import math
import datetime
pi = math.pi

def change(): # Calculate Money with amount of coins
    print("change counter \n")
    print("Enter your coins")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    print("your change is: ")
    print("     $", quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, sep="")

def quadratic(): # Quadratic equation
    lst = [] 
     
    n = int(input("Enter number of elements : ")) 
    
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input()) 
    
        lst.append(ele) # adding the element 
        
    print(np.roots(lst)) 

def numbers(n, r, a, p, q): # Different calculations
    print((3 + 4) * 5)
    print((n*(n-1)) / 2)
    print((4 * math.pi * r) ** 2) # Circle area
    print(math.sqrt(r*(math.cos(a)) + r*(math.sin(a)))) #
    print((p[0] - q[0]) / (p[1] - q[1])) # Slope calculation

def ranges(): # Ranges between numbers
    for i in range(5):
        print(i, sep="")
    print("--------")
    for i in range(3,10):
        print(i, sep="")
    print("--------")
    for i in range(4,13,3):
        print(i, sep="")
    print("--------")
    for i in range(15,5,-2):
        print(i, sep="")
    print("--------")
    for i in range(5,3):
        print(i, sep="")
    print("--------")

def Mults(): # Multiplying different numbers
    '''for i in [1,3,5,7,9]:
        print(i, ":", i**3)
    print(i)'''
    '''x = 2
    y = 10
    for j in range(0, y, x):
        print(j, end="")
        print(x + y)
    print("done")'''
    ans = 0
    for i in range(1,11):
        ans = ans + i*i
        print(i)
    print(ans)

def calculateDistance(x1,y1,x2,y2): # Distance between 2 2d point
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
def calculateVolume(r): # Calculate volum of sphere
    v = 4 / 3*pi*r**3
    a = 4*pi*r**2
    return str(v) + ", " + str(a)
def calculatePizzaPrice(price, diameter):
    Area = 4*pi*(diameter/2)**2
    return price / Area
def calcHydroCarbon(hydro, carbo, oxy):
    h = hydro * 1.0079
    c = carbo * 12.011
    o = oxy * 15.9994
    return h + c + o
def lightningDistance(timeBetweenStrike):
    dist = timeBetweenStrike * 1100
    return dist / 5280
def coffeeOrder(pounds):
    ppp = pounds * 10.50
    total = ppp + (0.86 * pounds) + 1.50
    return total
def calculateSlope(x1,y1,x2,y2):
    top = y2-y1
    bottom = x2-x1
    return str(top) + " / " + str(bottom)
date = datetime.datetime.now()
def daysToEaster():
    year = eval(input("Year: "))
    c = year / 100
    epact = (8 + (c/4) - c + ((8*c + 13)/25) + 11*(year%19))%30
    print(epact)
def calculateTriangleArea(a,b,c):
    s = (a+b+c) / 2
    ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(ar)

def ladderLength(angle, height):
    rads = math.pi / 180 * angle
    length = height / math.sin(rads)
    return length

def natrualNumbers():
    n = eval(input("Number: "))
    for i in range(1, n):
        print(i + i)

def cubeNumbers():
    n = eval(input("Number to be cubed: "))
    for i in range(1, n):
        print(i**n + i**n)

def addNumbers():
    nums = eval(input("Numbers to be summed: "))
    for i in range(1, nums):
        print(i+i)


def calculateSum():
    scores = list()
    scores_amount = input("Enter how many elements you want:") # Ask how many scores there are
    print ("Enter numbers in array: ") # ask what the scores are
    for i in range(int(scores_amount)): # does the calculation for each score
        n = input("Score: ")
        scores.append(int(n))
    current_score = 0
    for i in range(int(scores_amount)):
        if(i != 0):
            current_score = scores[i] + scores[i - 1] # adds the scores together
    print(current_score) # prints score once calculations are done

def calculateAverages():
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

def getPi():
    n = int(eval(input("How many times do you want to do this: ")))
    a = 1
    b = 4/a
    for i in range(0, n):
        a += 2
        if((i % 2) == 0):
            b -= 4/a
        else:
            b += 4/a
        print(str(a) + ": " + str(b) + " : " + str(math.pi - b))

def Fib(n): 
    if n<0: 
        print("Incorrect input") # Can't input 0
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fib(n-1)+Fib(n-2) 

def InputFib():
    l = int(eval(input("How many fibs? ")))
    for i in range(1, l):
        print(Fib(i))

def NewtonsMethod():
    x = eval(input("Square root value: "))
    amountToGuess = eval(input("How many times you want to guess? "))
    guess = x/2
    acutalAnswer = math.sqrt(x)
    for i in range(0, amountToGuess):
        if(not(math.isclose(guess, acutalAnswer, rel_tol=0.05))):
            guess = (guess + x/guess) / 2
            print("Guess " + str(i) + ": " + str(guess))
        else:
            print("The answer is about: ", guess)
    print(acutalAnswer)

        


def main():
    NewtonsMethod()
    

if __name__ == "__main__":
        main()