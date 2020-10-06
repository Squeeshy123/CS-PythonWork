#import numpy as np
import math

def change():
    print("change counter \n")
    print("Enter your coins")
    quarters = eval(input("Quarters: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    print("your change is: ")
    print("     $", quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01, sep="")

def quadratic():
    lst = [] 
     
    n = int(input("Enter number of elements : ")) 
    
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input()) 
    
        lst.append(ele) # adding the element 
        
    print(np.roots(lst)) 

def numbers(n, r, a, p, q):
    print((3 + 4) * 5)
    print((n*(n-1)) / 2)
    print((4 * math.pi * r) ** 2)
    print(math.sqrt(r*(math.cos(a)) + r*(math.sin(a))))
    print((p[0] - q[0]) / (p[1] - q[1]))

def main():
    numbers(10, 10, 50, [1,2], [3,4])
    #quadratic()

if __name__ == "__main__":
        main()