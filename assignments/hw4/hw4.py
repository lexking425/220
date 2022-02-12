"""
Lex King
hw4.py
wrote code to draw a square, rectangle, and cirlce. Also wrote code to compute pi.
this is my code
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = click.getX() - center.getX()
        dy = click.getY() - center.getY()
        copy = shape.clone()
        shape = copy
        shape.draw(win)
        shape.move(dx, dy)

        copy = shape.clone()
        shape = copy
        shape.draw(win)

    inst_pt = Point(width / 2, height - 100)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 750, 500)
    text = Text(Point(350, 10), "Click on two opposite points")
    text.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)
    rectangle.setOutline("green")
    rectangle.setFill("green")

    dx = abs(p1.getX() - p2.getY())
    dy = abs(p1.getY() - p2.getY())
    length = dx
    width = dy
    area = length * width
    perimeter = 2 * (length + width)

    box1 = Text(Point(50, 75), "Area:")
    box2 = Text(Point(50, 175), "Perimeter:")
    box1.draw(win)
    box2.draw(win)

    m1 = Text(Point(50, 100), area)
    m2 = Text(Point(50, 200), perimeter)
    m1.setTextColor("red")
    m2.setTextColor("red")

    m1.draw(win)
    m2.draw(win)

    message = Text(Point(350, 450), "click again to close.")
    message.draw(win)

    win.getMouse()
    win.close()

def circle():
    win = GraphWin("Circle", 700, 500)
    text = Text(Point(350, 10), "Click on two points to create a circle.")
    text.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    dx = abs(p1.getX() - p2.getX())
    radius = dx

    d = p2.getX() - p1.getX()
    y = p2.getY() - p1.getY()

    c1 = Circle(p1, radius)
    c1.draw(win)
    c1.setFill("Blue")

    distance = round(math.sqrt(d ** 2 + y ** 2), 2)
    m1 = Text(Point(350, 450), distance)
    box = Text(Point(350, 425),"Radius:")
    m1.setTextColor("red")
    m1.draw(win)
    box.draw(win)

    text = Text(Point(350, 250), "Click again to close")
    text.draw(win)

    win.getMouse()
    win.close()

def pi2():
    terms = eval(input("Enter the number of terms to sum:"))
    approx = -1
    pi = 0
    for i in range(terms):
        x = 2 * i + 1
        y = 4 / x
        approx = approx * -1
        pi = pi + y * approx
        accuracy = math.pi - pi
    print("Pi approximation:", pi)
    print("accuracy: ", accuracy)


if __name__ == '__main__':
    pass
