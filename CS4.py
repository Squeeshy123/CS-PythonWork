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


def dice():
    win = GraphWin("Dice", 800, 800)
    def drawDice(count, location, size):
        drawSquare(location.getX(), location.getY(), size, False, win)
        center = Point(location.getX() + (size/2), location.getY() + (size/2))
        if count == 1:
            Circle(center, 5).draw(win)
        if count == 2:
            Circle(Point(center.getX() + 10, center.getY()), 5).draw(win)
            Circle(Point(center.getX() - 10, center.getY()), 5).draw(win)
        if count == 3:
            Circle(Point(center.getX() + 15, center.getY()), 5).draw(win)
            Circle(Point(center.getX(), center.getY()), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY()), 5).draw(win)
        if count == 4:
            Circle(Point(center.getX() + 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() + 15, center.getY() - 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() - 15), 5).draw(win)
        if count == 5:
            Circle(Point(center.getX() + 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() + 15, center.getY() - 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() - 15), 5).draw(win)
            Circle(Point(center.getX(), center.getY()), 5).draw(win)
        if count == 6:
            Circle(Point(center.getX() + 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() + 15), 5).draw(win)
            Circle(Point(center.getX() + 15, center.getY() - 15), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY() - 15), 5).draw(win)
            Circle(Point(center.getX() + 15, center.getY()), 5).draw(win)
            Circle(Point(center.getX() - 15, center.getY()), 5).draw(win)

    for i in range(1,6):
        drawDice(randint(1, 6), Point((800 / 6) + (75 * i), 400), 50)
    win.getMouse()
    win.close()

def isInside(circle_x, circle_y, rad, x, y): 
      
    # Compare radius of circle 
    # with distance of its center 
    # from given point 
    if ((x - circle_x) * (x - circle_x) + 
        (y - circle_y) * (y - circle_y) <= rad * rad): 
        return True; 
    else: 
        return False; 

def CircleIntersection():
    cScale = 25
    cCenter = Point(400,410)

    randY1 = randint(0, 800)
    randY2 = randint(0, 800)

    win = GraphWin("Circle Intersection", 800, 800)


    c = Circle(cCenter, cScale)
    l = Line(Point(0, float(randY1)), Point(800, float(randY2))).draw(win)

    def reDraw():
        c = Circle(cCenter, cScale).draw(win)
        l = Line(Point(0, float(randY1)), Point(800, float(randY2))).draw(win)
    reDraw()


    def collisionUpdate():
        for x in range(0, 800):
            for y in range(randY1, randY2 + 1):
                if isInside(cCenter.getX(), cCenter.getY(), cScale, x, y):
                    Circle(Point(x,y), 1).draw(win)

    
    for i in range(0,100):
        mouse = win.getMouse()
        cCenter = Point(mouse.getX(),
                        mouse.getY())
        reDraw()
        collisionUpdate()

    win.getMouse()
    win.close()

def lower_point_y(p1, p2, switch):
    if p1.getY() > p2.getY():
        if switch:
            return p2
        else:
            return p1
    else:
        if switch:
            return p1
        else:
            return p2

def leftmost_Point_x(p1,p2,switch):
    if p1.getX() < p2.getX():
        if switch:
            return p2
        else:
            return p1
    else:
        if switch:
            return p1
        else:
            return p2

def LineInfo():
    win = GraphWin("Line Information", 800, 800)

    info1 = win.getMouse()
    x1 = info1.getX()
    y1 = info1.getY()

    info2 = win.getMouse()
    x2 = info2.getX()
    y2 = info2.getY()

    line = Line(Point(x1,y1), Point(x2,y2)).draw(win)
    dX = x2 - x1
    dY = y2 - y1

    midPoint = Circle(Point((x1+x2)/2, (y1+y2)/2), 5).draw(win)
    midPoint.setFill("cyan")
    slopePoint = Point(x1,y1)
    for i in range(0,1):
        if x1 != x2 or y1 != y2:
            slopePoint = Point(x2,y2)
            Line(Point(x1 + dX, y1), Point(x1,y1)).draw(win)
            Line(Point(x1 + dX, y1), Point(x1 + dX, y1 + dY)).draw(win)

    slopeInfo = Text(Point(100, 100), 15).draw(win)
    slopeInfo.setText(str(int(abs(dX))) + " / " + str(int(abs(dY))))
    win.getMouse()


def rectangleInfo():
    win = GraphWin("Rectangle Information", 800, 800)

    p1 = win.getMouse()
    p2 = win.getMouse()
    width = abs(p1.getX() - p2.getX())
    length = abs(p1.getY() - p2.getY())

    perimeter = 2*(width+length)
    area = length*width

    rect = Rectangle(p1,p2).draw(win)

    Text(Point(100,100), "Perimeter: " + perimeter).draw(win)
    Text(Point(100,150), "Area: " + area).draw(win)



def House():
    win = GraphWin("Build a house", 800, 800)
    p1 = win.getMouse()
    p2 = win.getMouse()
    width = abs(p1.getX() - p2.getX())
    base = Rectangle(p1,p2).draw(win)
    doorp = win.getMouse()
    lowerp = lower_point_y(p1,p2, False)
    midpoint = Point((base.getP1().getX() + base.getP2().getX())/2, (base.getP1().getY() + base.getP2().getY())/2)
    Rectangle(Point(doorp.getX() - ((width/5) / 2), lowerp.getY()), Point(doorp.getX() + ((width/5) / 2), doorp.getY())).draw(win)
    roof = win.getMouse()
    bp1 = base.getP1()
    bp2 = base.getP2()
    Polygon(Point(leftmost_Point_x(bp1,bp2, False).getX(), lower_point_y(bp1,bp2, True).getY()), Point(leftmost_Point_x(bp1,bp2, True).getX(), lower_point_y(bp1,bp2, True).getY()), Point(midpoint.getX(), roof.getY())).draw(win)
    window = win.getMouse()
    Rectangle(Point(window.getX() + ((width/5) / 4), window.getY() + ((width/5) / 4)), Point(window.getX() - ((width/5) / 4), window.getY() - ((width/5) / 4))).draw(win)
    win.getMouse()
    

def distance(p1,p2):
    return math.sqrt(abs((p1.getX() - p2.getX()) + (p1.getY() - p2.getY())))

def triangleInfo():
    win = GraphWin("Triangle Information", 800, 800)
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    Polygon(p1,p2,p3).draw(win)
    a = distance(p1,p2)
    b = distance(p2,p3)
    c = distance(p3,p1)



    s = ( a + b + c ) / 2
    print(s*(s-a)*(s-b)*(s-c))
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    Text(Point(100,100), "Area: " + str(area)).draw(win)
    Text(Point(120, 150), "A side: " + str(a) + "\nB Side: " + str(b) + "\nC Side: " + str(c)).draw(win)

    win.getMouse()


def TicTacToe():
    pass

def main():
    House()
main()