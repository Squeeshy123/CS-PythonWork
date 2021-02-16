from random import *
from itertools import permutations 

def commacount():
    print("This program counts commas given a file.")
    file_input = input("What file do you want to know how many commas are in?")
    file_read = open(file_input, 'r')
    read_file = file_read.read()

    count = 0
    for i in range(0, len(read_file)):
        if read_file[i] == ',':
            count += 1
    if count == 0:
        print("There are no commas in this file")
    else:
        print("There are " + str(count) + " comma in this file")

def combs():
    comb = permutations([1, 0, 2], 6)
    print(list(comb))
    for i in list(comb):
        print (i)
combs()