from graphics import *
from random import *
import math


def InvestmentGraph():
    win = GraphWin('Business and Deals', 800, 800)

    investments = [10,2,25,53,100]
    Yscale = -2
    width = 40
    baseY = 280
    addx = 40
    for i in range(0,len(investments)):
        baseX = i*width
        rect = Rectangle(Point(baseX + addx, baseY), Point(baseX + addx + width, baseY + investments[i] * Yscale))
        rect.setFill("grey")
        rect.draw(win)
    maxi = max(investments)
    divisions = len(investments)
    Text(Point(100, 100), "Hey")
    for i in range(1, int(divisions) + 1):
        Text(Point(20, investments[i-1] * Yscale + baseY ), str(investments[i-1])).draw(win)
        print(str(230 - -i * 50))
    
    win.getMouse()
    win.close()

def GetIndex(row, col, width):
    return width * row + col


def drawSquare(x, y, size, state, window):
    square = Rectangle(Point(x, y), Point(x + size, y + size))
    if(state):
        square.setFill('black')
    else:
        square.setFill('white')
    square.draw(window)
    return square


def getUp(array, index, width):
    return array[index-1]
def getDown(array, index, width):
    return array[index+1]
def getLeft(array, index, width):
    return array[index-width]
def getRight(array, index, width):
    return array[index+width]

def Cells(): # Testing Cellular Automata
    win = GraphWin('Cellular Automata', 800, 800)
    Cells = []
    sizeX = 10
    sizeY = 10
    size = 50
    history = []

    for x in range(0, sizeX):
        for y in range(0, sizeY):
            square = drawSquare(x * size, y * size, size, False, win) # bool(getrandbits(1))
            Cells.append(square)
    for x in Cells:
        text = Text(Point(x.getP1().getX() + 10,x.getP1().getY() + 10), str(Cells.index(x))) #

        text.draw(win)
    def pickFirst():
        index = randrange(len(Cells))
        Cells[index] = drawSquare(Cells[index].getP1().getX(), Cells[index].getP1().getY(), size, True, win)
        print("First: " + str(index))
        history.append(Cells[index])
        return Cells[index]
    
    pickFirst()
    
    def GenerateFrom():
        index = Cells.index(getUp(Cells, Cells.index(history[0]), sizeX))
        Cells[index] = drawSquare(Cells[index].getP1().getX(), Cells[index].getP1().getY(), size, True, win)
        previous = history[0]
        print("Second: " + str(index))
        direction = randrange(3)
        if direction == 0:
            history.append(getUp(Cells, Cells.index(previous), sizeX))
        elif direction == 1:
            history.append(getLeft(Cells, Cells.index(previous), sizeX))
        elif direction == 2:
            history.append(getRight(Cells, Cells.index(previous), sizeX))
        elif direction == 3:
            history.append(getDown(Cells, Cells.index(previous), sizeX))
    generations = 2
    for i in range(0, generations):
        GenerateFrom()
        for c in history:
            #history[Cells.index(c)] = drawSquare(history[Cells.index(c)].getP1().getX(), history[Cells.index(c)].getP1().getY(), size, True, win)
            pass
    #print(Cells)
    win.getMouse()
    win.close()



def ClickingCircles():
    win = GraphWin ()
    shape = Circle (Point (50,50), 20)
    shape.setOutline("red")
    shape. setFill("red")
    shape.draw (win)
    for i in range (10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move (dx,dy)
    win.close ()

def ClickingSquares():
    win = GraphWin ()
    shape = drawSquare(100, 100, 25, False, win)
    shape.setOutline("red")
    shape.setFill("red")
    for i in range (10):
        p = win.getMouse()
        c = shape.getCenter()
        drawSquare(c.getX() - (25/2), c.getY() - (25/2), 25, False, win)
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move (dx,dy)
        if(i == 8):
            Text(Point(25,25), 'Click Again to quit').draw(win)
    win.close ()

def TargetPractice():
    win = GraphWin("Target", 800, 800)
    size = 40
    for i in range(0, 10):
        c = Circle(Point(400, 400), size*10 - (i*size))
        c.draw(win)
        if i%2 == 0:
            c.setFill("red")
        else:
            c.setFill("white")
    win.getMouse()
    win.close()

def drawTrapezoid(center, bottomWidth, topWidth, height, win):
    t = Polygon(Point(center.getX() + bottomWidth, center.getY()), Point(center.getX() - bottomWidth, center.getY()), Point(center.getX() - topWidth, center.getY() - height), Point(center.getX() + topWidth, center.getY() - height)).draw(win)
    t.setFill("green")
    t.setOutline("green")

def Face():
    win = GraphWin('Face',300,300)

    f = Oval(Point(75,50),Point(225,250))
    f.setFill('pink')
    f.draw(win)

    el = Circle(Point(120,120),15)
    el.setFill('white')
    el.draw(win)
    ebl = Circle(Point(120,120),5)
    ebl.setFill('black')
    ebl.draw(win)

    er = Circle(Point(180,120),15)
    er.setFill('white')
    er.draw(win)
    ebr = Circle(Point(180,120),5)
    ebr.setFill('black')
    ebr.draw(win)

    n = Oval(Point(110,185),Point(190,225))
    n.setFill('black')
    n.draw(win)

    n = Oval(Point(125,110),Point(175,190))
    n.setFill('pink')
    n.draw(win)

    win.getMouse()
    win.close()

def Winter():
    win = GraphWin("Target", 400, 400)
    #drawTrapezoid(Point(200, 200), 100, 75, 25, win)
    def DrawTree(center, height, trunkWidth):
        r = Rectangle(Point(center.getX() - trunkWidth, center.getY()), Point(center.getX() + trunkWidth, center.getY() + height)).draw(win)
        r.setFill("brown")
        r.setOutline("brown")
        for x in range(0, 5):
            i = 5-x
            drawTrapezoid(Point(center.getX(), (center.getY() - 50) + i*height), i*7, i*2, i*5, win)
    def drawSnowman(center, size):
        Circle(center, size*3).draw(win)
        Circle(Point(center.getX(), center.getY() - size), size*2).draw(win)
        Circle(Point(center.getX(), center.getY() - size*2), size).draw(win)

        
    sky = Rectangle(Point(0,0), Point(400, 200)).draw(win)
    sky.setFill(color_rgb(0, 184, 230))
    sky.setOutline(color_rgb(0, 184, 230))
    for i in range(0, 10):
        DrawTree(Point(randrange(0, 400),randrange(200, 400)), 11, 5)
    drawSnowman(Point(200,100), 20)

    

    win.getMouse()
    win.close()

def main():
    TargetPractice()
main()