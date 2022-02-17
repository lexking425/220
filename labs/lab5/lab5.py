'''
Lex King
lab5.py
in this code you can draw a triangle, make any color circle, made strings and lists, and made a dart board.
this is my code
'''
import math

from graphics import *

def triangle():
    win = GraphWin("Triangle", 500, 500)
    text = Text(Point(350, 10), "Click on three points to draw a triangle")
    text.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)
    triangle.setFill('red')

    dx_1 = (p1.getX() - p2.getX())
    dy_1 = (p1.getY() - p2.getY())
    length_1 = math.sqrt(dx_1 ** 2 + dy_1 ** 2)
    dx_2 = (p2.getX() - p3.getX())
    dy_2 = (p2.getY() - p3.getY())
    length_2 = math.sqrt(dx_2 ** 2 + dy_2 ** 2)
    dx_3 = (p3.getX() - p1.getX())
    dy_3 = (p3.getY() - p1.getY())
    length_3 = math.sqrt(dx_3 ** 2 + dy_3 ** 2)
    perimeter = length_1 + length_2 + length_3

    s = perimeter / 2
    area = (s * (s - length_1) * (s - length_2) * (s - length_3))
    final_area = math.sqrt(area)

    box1 = Text(Point(50, 175), "Perimeter:")
    box2 = Text(Point(50, 75), "Area:")
    box1.draw(win)
    box2.draw(win)
    m1 = Text(Point(75, 200), perimeter)
    m2 = Text(Point(75, 100), final_area)
    m1.draw(win)
    m2.draw(win)

    message = Text(Point(350, 450), "click again to close.")
    message.draw(win)

    win.getMouse()
    win.close()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_input = Entry(Point(win_width / 2, win_height / 2 + 40), 5)
    red_input.draw(win)
    green_input = Entry(Point(win_width / 2, win_height / 2 + 70), 5)
    green_input.draw(win)
    blue_input = Entry(Point(win_width / 2, win_height / 2 + 100), 5)
    blue_input.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_input.getText())
        green = int(green_input.getText())
        blue = int(blue_input.getText())

        color = color_rgb(red, green, blue)
        shape.setFill(color)

    msg2 = "click to close window"
    box = Text(Point(win_width / 2, win_height - 50), msg2)
    box.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string = input("Input a string: ")
    print(string[0])
    print(string[-1])
    print(string[1:5])
    print(string[0], "+", string[-1],"=", string[0] + string[-1])
    print(10 * string[0:3])
    for i in string:
        print(i, end = '\n')
    print(len(string))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print(values[1] + values[3])
    print(values[0] + values[2])
    print(5 * values[1])
    print(values[2:5])
    print(values[2:4], values[0])
    print(values[2], values[0], float(values[5]))
    print(values[0] + values[2] + float(values[5]))
    print(len(values))

def another_series():
    amount = eval(input("how many terms would you like? "))
    sum = 0
    for i in range(amount):
        terms = i % 3 * 2 + 2
        sum = sum + terms
        print(terms, end = ' ')
    print("sum =", sum)


def target():
    win = GraphWin("Target", 500, 500)
    yellow_center = Point(250, 250)
    yellow = Circle(yellow_center, 50)

    red_center = Point(250, 250)
    red = Circle(red_center, 100)

    blue_center = Point(250, 250)
    blue = Circle(blue_center, 150)

    black_center = Point(250, 250)
    black = Circle(black_center, 200)

    white_center = Point(250, 250)
    white = Circle(white_center, 250)

    # for i in range(6):
    #     center_point = Point(250, 250)
    #     radius = center_point + 50

    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)

    white.setFill('white')
    black.setFill('black')
    blue.setFill('blue')
    red.setFill('red')
    yellow.setFill('yellow')


