from graphics import *


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


def main():
    InvestmentGraph()
main()