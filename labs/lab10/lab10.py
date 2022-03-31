'''
Lex King
lab10.py

this is my code
'''

from random import choice
from graphics import Rectangle, GraphWin, Point, Text
from button import Button
from door import Door

def main():
    win = GraphWin("Three Door Game", 400, 400)

    button = Rectangle(Point(100, 50), Point(300, 100))
    working_button = Button(button)
    working_button.draw(win)

    door = Rectangle(Point(100, 120), Point(300, 400))
    working_door = Door(door)
    working_door.draw(win)

    open = Text(Point(200, 250), "Open")
    closed = Text(Point(200, 250), "Closed")

    click = win.getMouse()

    if door == open:
        Door.color_door("white")
    else:
        Door.color_door("red")