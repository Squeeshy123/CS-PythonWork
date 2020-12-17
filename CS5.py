from string import *
import numpy as np

def inRange(num, min, max): # NITQ
    if num > min and num < max:
        return True
    else:
        return False


def dateconvert(): # PE 1
    pass 



# Make user friendly!!

def CSProffessor1(): # PE 2
    print("---CS Proffessor Grade Converter---")
    letter_grades = ['A','B','C','D','F','F'] # List of possible grades
    in_grade = eval(input("Input the students grade: ")) # Check for students grade
    if in_grade <= 5 and in_grade >= 0: # Check if the grade is valid
        print(letter_grades[-in_grade - 1]) # Gets the grade corrosponding to that number
    else:
        print("Invalid Grade")
def CSProffessor2(): # PE 3
    print("--CS Professor Grade Converter V2---")
    in_grade = eval(input("Input the students grade: "))
    grade = ['A','B','C','D','F'] # List of possible grades
    if inRange(in_grade, 90, 100):
        print(grade[0])
    else:
        if inRange(in_grade, 80, 89):
            print(grade[1])
        else:
            if inRange(in_grade, 70, 79):
                print(grade[2])
            else:
                if inRange(in_grade, 60, 69):
                    print(grade[3])
                else:
                    if in_grade < 60:
                        print(grade[4])



def AcronymGenerator(): # PE 4
    print("---Acronym Generator---")
    phrase = input("What is your phrase? ")
    acro = phrase[0]
    for i in range(0, len(phrase)):
        if phrase[i] == ' ':
            acro += phrase[i+1]
    print(acro.upper())

def NumericalNameGenerator(): # PE 5 and 6
    print("Numerologist claim that they can predict character traits based on your names \"numerical value\"")
    name = input("What's your name? ")
    value = 0
    for i in range(0, len(name)):
        value += ascii_lowercase.find(name[i].lower()) + 1
    print("Your name's numerical value is: " + str(value))

def CaeserCipher(): # PE 7 and 8
    print("Caeser Cipher Encoder: A Message encoded with a shift amount, so if your message was hello and your shift amount was 1, then the message would be ifmmp") # PE 7
    encode_or_decode = input("Would you like the encode or decode? ")
    if encode_or_decode == "encode":
            message = input("Type the message you want to encode: ")
            key = ascii_letters
            shift_amount = eval(input("How much would you like to shift the cipher? "))
            temp = ""
            for i in range(0, len(message)):
                if message[i] in key:    
                    if message[i] == ' ':
                        temp = temp + " "
                    else:
                        if (key.find(message[i]) + shift_amount) > len(key):
                            temp = temp + key[(key.find(message[i]) + shift_amount) - len(key)]
                        else:
                            temp = temp + key[key.find(message[i]) + shift_amount]
                else:
                    temp = temp + message[i]
            print(temp)

    if encode_or_decode == "decode":
        message = input("Type the message you want to decode: ")
        key = ascii_letters
        shift_amount = eval(input("What is this codes shift amount? ")) * -1
        temp = ""
        for i in range(0, len(message)):
            if message[i] == ' ':
                temp = temp + " "
            else:
                if message[i] not in key:
                    temp = temp + message[i]
                else:
                    temp = temp + key[key.find(message[i]) + shift_amount]
            
        print(temp)

def WordCounter(): # PE 9
    print("Word Counter: Count the amount of words used in a sentance.")
    sentance = input("What sentance do you need word counting for? ")
    count = 1
    for i in range(0, len(sentance)):
        if sentance[i] == ' ':
                    count += 1
    print(count)
def wordAverage(): # PE 10
    print("Word Counter: Count the amount of words used in a sentance.")
    sentance = input("What sentance do you need word counting for? ")
    count = 1
    word_length = []
    for i in range(0, len(sentance)):
        word_length.append(0)
        if sentance[i] == ' ':
                    count += 1
        else:
            word_length[count-1] += 1
    print(np.mean(word_length))

def calculateChaos(number, loops):
    indexes = [3.9 * number * (1-number)]
    for i in range(1, loops):
        indexes.append(3.9 * (indexes[i-1]) * (1-indexes[i-1]))
    return indexes


def chaos(): # PE 11
    print("Calcualate the Chaos of floating point values.") # output
    numbers = eval(input("How Many numbers would you like to calculate? ")) # Input
    num = []
    for a in range(numbers):
        x = eval(input("What are the numbers? (keep them between 0 and 1): ")) # Input
        num.append(x)
    loops = eval(input("How many times would you like to calculate them? "))
    print("\n")
    fin = "  "
    
    for x in range(numbers):
        fin = fin + " " + str(num[x])
        for i in range(5 - len(str(num[x]))):
            fin = fin + "0"
        fin = fin + " "
    sep = "\n-"
    for b in range(len(fin)):
        sep = sep + "-"
    print(fin + sep)
    fin = ""
    for y in range(loops):
        fin = fin + "\n" + str(y) + ": "
        for z in range(len(num)):
            fin = fin + str(3.9 * num[z] * (1-num[z]))[:5] + "  "
            num[z] = 3.9 * num[z] * (1-num[z])

    print(fin)


def Linux_WC():
    File_path = input("What file to read? ")
    f = open(File_path, 'r')
    string = f.read()
    count = 1
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    if count == 1:
        print("Found " + str(count) + " word.")
    else:
        print("Found " + str(count) + " words.")
    print(string)
    f.close()



    

Linux_WC()