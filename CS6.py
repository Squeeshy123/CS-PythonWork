# Page 170

## RUN THESE PROGRAMS YOURSELF


from graphics import *


def mcdonald(): # PE 1: Prints old mcdonald had a farm
    def yodel():
        return " Ee-igh, Ee-igh, oh"
    def farm_animal(animal, animal_noise):
        print("and on that farm he had a " + animal + yodel())
        noise_combo = animal_noise + ", " + animal_noise + " there"
        print("with a " + noise_combo + " and a " + noise_combo)
        print("old mcdonald had a farm" + yodel())

    print("old mcdonald had a farm" + yodel())

    farm_animal("cow", "moo")
    farm_animal("pig", "oink")
    farm_animal("chicken", "bawk")
    farm_animal("dog", "bark")
    farm_animal("cat", "meow")
    
def ants_go_marching(spice_lines): # PE 2 Ants go marching
    def one_by_one():
        return "the ants go marching one by one"
    def hurrah():
        return ", hurrah! hurrah!"
    def end_verse():
        return "and they all go marching down... \nIn the ground... \nTo get out... \nOf the rain... \nBoom! Boom! Boom!"
    
    def first_section(spice):
        final = one_by_one() + hurrah() + "\n"
        final += final
        final += one_by_one() + ",\n"
        final += spice + ",\n"
        return final
    for i in spice_lines:
        print(first_section(i) + end_verse())

def sphereArea(radius): # PE 3 Sphere area and volume
    return pow((4*PI*radius), 2)
def sphereVolume(radius):
    return (4*PI*radius) 

def sumN(n): # PE 4 sumN and sumNCubes
    a = 0
    for i in range(n):
        a += i+1
        print(i+1)
    return a

def sumNCubes(n):
    a = 0
    for i in range(n):
        a += pow(i+1, 3)

def squareEach(nums): # PE 11 
    for i in range(len(nums)):
        nums[i] = pow(nums[i], 2)
    return nums

def sumList(list): # PE 12
    a = 0
    for i in list:
        a += i
    return a
def toNumbers(list): # PE 13
    for i in range(len(list)):
        list[i] = float(list[i])
    return list
def drawFace(c, size, win): # PE 14
    Circle(c, size).draw(win)
    Circle(Point(c.x, c.y + size/2), size/10).draw(win)
    Circle(Point(c.x + size/2, c.y - size/5), size/15).draw(win)
    Circle(Point(c.x - size/2, c.y - size/5), size/15).draw(win)
    # Run face_program to test this function

def face_program():
    graphwin = GraphWin("hello",250,250)
    drawFace()
    graphwin.getMouse()

def moveTo(shape, newCenter):
    shape.move(newCenter.x - shape.getCenter().x, newCenter.y - shape.getCenter().y)
    # Run moving_program to test this function.

def moving_program():
    graphwin = GraphWin("hello",250,250)

    c = Circle(Point(50,50), 10).draw(graphwin)

    for i in range(10):
        moveTo(c, graphwin.getMouse())

    graphwin.getMouse()
